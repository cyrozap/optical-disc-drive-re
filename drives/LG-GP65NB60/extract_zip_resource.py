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
