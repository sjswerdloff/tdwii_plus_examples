#!/usr/bin/env python
"""generate a UID that can be used as a transaction UID"""


from pydicom import uid

if __name__ == "__main__":
    print(uid.generate_uid())
