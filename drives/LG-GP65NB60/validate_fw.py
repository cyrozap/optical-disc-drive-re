#!/usr/bin/env python3

import argparse
import struct
import sys

try:
    import mt1887_fw
except ModuleNotFoundError:
    print("Error: Failed to import \"mt1887_fw.py\". Please run \"make\" in this directory to generate that file, then try running this script again.", file=sys.stderr)
    sys.exit(1)


def checksum(data : bytes):
    csum = 0
    for (val,) in struct.iter_unpack('<H', data):
        csum += val
    csum &= 0xffff
    return csum

def validate_checksum(name : str, data : bytes, expected : int):
    calc_csum = checksum(data)
    exp_csum = expected
    if calc_csum != exp_csum:
        print("Error: Invalid {} checksum: expected 0x{:04x}, got: 0x{:04x}".format(name, exp_csum, calc_csum), file=sys.stderr)
        sys.exit(1)
    print("{} checksum OK!".format(name))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("firmware", type=str, help="The MT1887 firmware binary.")
    args = parser.parse_args()

    fw_bytes = open(args.firmware, 'rb').read()
    fw = mt1887_fw.Mt1887Fw.from_bytes(fw_bytes)

    validate_checksum("ARM", fw.fw_arm, fw.checksum)


if __name__ == "__main__":
    main()
