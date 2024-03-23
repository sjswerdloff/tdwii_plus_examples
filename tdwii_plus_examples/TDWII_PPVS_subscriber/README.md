# TDWII_PPVS_SUBSCRIBER

A PySide6 (PyQT) based UI that acts as a 3rd party in TDW-II, with the ability to:
1. issue a C-FIND to get the UPS with matching machine name and scheduled date time.
2. issue a C-MOVE request to get the referenced objects
3. Receive and cache the moved referenced objects (C-STORE SCP)
4. Subscribe and unsubscribe for UPS (initially just Global subscription)
