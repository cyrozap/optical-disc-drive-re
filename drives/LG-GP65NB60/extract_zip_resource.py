#!/usr/bin/env python3

import argparse
import struct


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str, default="extracted.zip", help="Output zip.")
    parser.add_argument("input", type=str, help="Input binary.")
    parser.add_argument("start", type=int, help="Zip file offset.")
    parser.add_argument("length", type=int, help="Zip file length.")
    args = parser.parse_args()

    binary = open(args.input, 'rb').read()
    zip_start = args.start
    zip_length = args.length
    zip_raw = binary[zip_start:zip_start+zip_length]
    zip_extracted = bytearray(zip_length)

    for i, (val,) in enumerate(struct.iter_unpack('<H', zip_raw[:-(zip_length % 2)])):
        struct.pack_into('>H', zip_extracted, i * 2, val)

    if (zip_length % 2) != 0:
        zip_extracted[-1] = zip_raw[-1]

    open(args.output, 'wb').write(zip_extracted)
