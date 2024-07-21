# StoreSCU.py
import logging

from pydicom import Dataset

# from pydicom.errors import InvalidDicomError
# from pydicom.uid import UID
from pynetdicom import AE  # , Association, UnifiedProcedurePresentationContexts
from pynetdicom.presentation import build_context

from tdwii_plus_examples import tdwii_config


class NSetSCU:
    def __init__(
        self,
        sending_ae_title: str,
        receiving_ae_title: str,
    ):
        self.calling_ae_title = sending_ae_title
        self.receiving_ae_title = receiving_ae_title
        tdwii_config.load_ae_config()

    def n_set_ups(self, n_set_ds: Dataset, receiving_ae_title: str = None) -> tuple[bool, list[Dataset]]:
        """Used for RO-62 Progress Update and RO-64 Final Update, also see
        DICOM Part 4, CC.1.1 Unified Procedure Step States and
        Table CC.2.5-3. UPS SOP Class N-CREATE/N-SET/N-GET/C-FIND Attributes

        Args:
            n_set_ds (Dataset): The dataset containing the normalized IOD used to update the UPS
                                Must have SOP Class UID set to UPS Push or a UPS class that the SCP will accept for N-SET-RQ
                                Must have Affected SOP Instance UID set to match the UPS it is updating
                                Must have the Transaction UID for the UPS that is IN PROGRESS
                                There are specific elements that must not be encoded per Table CC.2.5-3
            receiving_ae_title (str, optional): The TMS AE Title. Defaults to None, indicating that the value
                                used for receiving_ae_title when instantiating the NSetSCU class/object is appropriate.

        Returns:
            bool: True if the N-SET succeeded, False otherwise
            list(Dataset): The N-SET-RSP content in a list, possibly empty if the N-SET didn't succeed
        """
        ae = AE(ae_title=self.calling_ae_title)
        dest_ae_title = self.receiving_ae_title
        if receiving_ae_title is not None:
            dest_ae_title = receiving_ae_title
        contexts_in_iods = [build_context(n_set_ds.AffectedSOPClassUID)]
        assoc = ae.associate(
            tdwii_config.known_ae_ipaddr[dest_ae_title],
            tdwii_config.known_ae_port[dest_ae_title],
            contexts=contexts_in_iods,
            ae_title=dest_ae_title,
        )
        success = False
        if assoc.is_established:
            info_message = f"Association established with {dest_ae_title}"
            logging.info(info_message)
            msg_id = 0
            success = True
            ups_responses = list()
            msg_id += 1
            responses = assoc.send_n_set(
                n_set_ds,
                n_set_ds.AffectedSOPClassUID,
                n_set_ds.AffectedSOPInstanceUID,
                msg_id=msg_id,
                meta_uid=n_set_ds.AffectedSOPClassUID,
            )
            for status, response_content in responses:
                if status and status.Status in [0xFF00, 0xFF01]:
                    ups_responses.append(response_content)
                elif status is None or status.Status != 0x0000:
                    success = False
                    error_msg = "No response at all from {dest_ae_title} to N-SET-RQ"
                    if status is not None:
                        error_msg = f"Failed with status {status.Status} \
                            when trying to issue n-set for {n_set_ds.AffectedSOPInstanceUID} \
                                to {dest_ae_title}"
                    logging.error(error_msg)

            assoc.release()
            info_message = f"Released association with {receiving_ae_title}"
            logging.info(info_message)
        return success, ups_responses


if __name__ == "__main__":
    from pydicom import Sequence
    from pynetdicom.sop_class import UnifiedProcedureStepPush

    scu = NSetSCU("TDD", "TMS")
    ds = Dataset()
    ds.AffectedSOPInstanceUID = "1.2.826.0.1.3680043.8.498.99261692600362543248321113263925080531"
    ds.AffectedSOPClassUID = UnifiedProcedureStepPush
    ds.TransactionUID = "1.2.3.4.5.6.7.8.9"
    ds.RequestedSOPClassUID = UnifiedProcedureStepPush
    ds.RequestedSOPInstanceUID = "1.2.826.0.1.3680043.8.498.99261692600362543248321113263925080531"
    update_ds = Dataset()
    update_ds.ProcedureStepProgressInformationSequence = Sequence()
    info_seq_item = Dataset()
    update_ds.ProcedureStepProgressInformationSequence.append(info_seq_item)
    info_seq_item.ProcedureStepProgress = 1.0
    UPSPerformedProcedureSequence = Sequence()
    # update_ds[(0x0074,0x1216)] = Sequence()
    update_ds.UnifiedProcedureStepPerformedProcedureSequence = UPSPerformedProcedureSequence
    output_info_seq = Sequence()
    perf_pro_seq_item = Dataset()
    update_ds.UnifiedProcedureStepPerformedProcedureSequence.append(perf_pro_seq_item)
    perf_pro_seq_item.OutputInformationSequence = Sequence()
    ds.update(update_ds)
    scu.n_set_ups(ds)
