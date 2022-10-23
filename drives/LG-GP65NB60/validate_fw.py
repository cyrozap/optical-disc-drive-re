#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD

# Copyright (C) 2021 by Forest Crossman <cyrozap@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
# AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
# DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
# PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.


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
