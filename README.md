# tdwii-plus-examples
Working python sample code for performing various transactions within the IHE-RO TDW-II profile, as well as extensions based on UPS Watch and UPS Event
No claims are being made that any of the sample code is adherent to the profile,
but the examples that are not UPS Watch/UPS Event should interact successfully within limits with valid TDW-II actors.

The sample queries and responses are not necessarily coordinated with an OST (yet), i.e. using an appropriate AE Title

Application entity information now in a configuration file

Text files in dcmdump format for various queries.
## dcmdump and dump2dcm are in dcmtk, typically available
on linux using:
```console
sudo apt install dcmtk
```
or
on MacOS using:
```console
brew install dcmtk
```
To generate .dcm files needed by ups enabled findscu
```console
dump2dcm queryfile.dcmdump.txt queryfile.dcm
```

## A sample C-FIND SCU is available from pynetdicom (it has been enhanced with support for UPS): clone from https://github.com/pynetdicom/pynetdicom.git
then use findscu to query the TMS (Treatment Management System):

in pynetdicom/apps

```console
python findscu.py --ups -f UPSCFind_TDWII_SCHEDULED_FX1.dcm 10.211.55.8 10401

```
Assuming the TMS has a session scheduled for machine FX1, this should result in a response file
rsp000001.dcm

use that response to drive a C-MOVE-RQ:

## A script that will issue a C-MOVE-RQ for the referenced inputs in the previous response
The following will send the C-MOVE-RQ to the AE Title listed (in the C-FIND-RSP e.g. in the rsp000001.dcm file above) for a given input information sequence item and specify PPVS_SCP as the destination for the move
```console
python cmove_inputs.py PPVS_SCP ../../pynetdicom/pynetdicom/apps/findscu/rsp000001.dcm
```

Note that the IP Address and Port information for a given Application Entity (e.g. PPVS_SCP as shown above) must be configured in the ApplicationEntities.json file.

## A TMS Simulator (of very limited capability) is provided in upsscp.py:
in tdw-plus-examples/
```console
python upsscp.py --debug

```
The default configuration will specify a ups_instances directory that upsscp will read from to find responses it will provide to queries that match them.

The default configuration listens on port 11114

Matching/filtering is currently based only on Scheduled Station Name (machine name) and Procedure Step Status.

A sample response is in tdw-plus-examples/responses/dcm and it can be renamed and then copied in to ups_instances before starting upsscp

Alternative/additional sample responses can be constructed by using dcmdump on the provided sample response, editing the text, and using dump2dcm.

For files to be found in ups_instances by upsscp, the response files must be named according to UPS_\<SOPInstanceUID\>.dcm

There is a utility script rename_ups_response.py that takes the response file as input and creates as output a file whose name is in the format required.

So one could test without having a real TMS:
```console
python findscu.py --ups -f UPSCFind_TDWII_SCHEDULED_FX1.dcm 127.0.0.1 11114

```


## A sample UPS Watch SCU (for subscribing for UPS Event/notification) is provided in watchscu.py
```console
python watchscu.py 127.0.0.1 11114

```
the above will attempt to perform a Global Subscription to upsscp



## A sample application for receiving notifications (N-EVENT-REPORT-RQ) is provided in neventscp.py
```console
python neventscp.py --debug

```
which listens on port 11115 by default,

The application does not take specific actions when receiving an N-EVENT-REPORT (but it will log in response)



## A sample application for sending notifications is provided in neventscu.py (which can be run against neventscp.py mentioned above)
```console
python neventscu.py 127.0.0.1 11115

```

## The OST can be simulated using the pynetdicom qrscp application.

The intent is to eventually integrate the various functionality as appropriate in to a TMS Simulator and a PPVS Simulator (and perhaps eventually a TDS Simulator).

But the purpose of the examples is to provide working sample code for individual TDW-II Transactions and for UPW Watch/UPS Event capabilities that can be used to extend a TDW-II environment so that it is event aware/event driven.
