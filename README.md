# tdwii-plus-examples
Working python sample code for performing various transactions within the IHE-RO TDW-II profile, as well as extensions based on UPS Watch and UPS Event

Application entity information now in a configuration file

Text files in dcmdump format for various queries.
dcmdump and dump2dcm are in dcmtk, typically available 
on linus using:
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

then use findscu to query the TSM:

in pynetdicom/apps

```console
python findscu.py --ups -f UPSCFin_TDWII_SCHEDULED_FX1.dcm 10.211.55.8 10401

```
Assuming the TMS has a session scheduled for machine FX1, this should result in a response file
rsp000001.dcm

use that response to drive a C-MOVE-RQ:
The following will send the C-MOVE-RQ to the AE Title listed for a given input information sequence item and specify PPVS_SCP as the destination for the move
```console
python cmove_inputs.py PPVS_SCP ../../pynetdicom/pynetdicom/apps/findscu/rsp000001.dcm
```


