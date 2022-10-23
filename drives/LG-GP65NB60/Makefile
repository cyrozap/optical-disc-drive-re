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


all: mt1887_fw.py HLDS_RUP3_GP65NB60_BRAND_PB01-05.bin

%.py: %.ksy
	kaitai-struct-compiler -t python $<

GP65NB60_SVC-Code-NB60_PB01.zip:
	curl -o $@ 'https://gscs-b2c.lge.com/downloadFile?fileId=msh2u1B45xbhf6lGTrGQ8Q'

GP65NB60_SVC-Code-NB60_PB01.exe: GP65NB60_SVC-Code-NB60_PB01.zip GP65NB60_SVC-Code-NB60_PB01.zip.sha256sum
	sha256sum -c $<.sha256sum
	unzip -DD $<
	mv "GP65NB60_SVC Code NB60_PB01.exe" $@

HDLSBIN.ZIP: GP65NB60_SVC-Code-NB60_PB01.exe extract_zip_resource.py
	python3 extract_zip_resource.py -o $@ $< 2912140 932363

HLDS_RUP3_GP65NB60_BRAND_PB01-05.bin: HDLSBIN.ZIP
	unzip -DD $<

clean:
	rm -f mt1887_fw.py HLDS_RUP3_GP65NB60_BRAND_PB01-05.bin HDLSBIN.ZIP GP65NB60_SVC-Code-NB60_PB01.exe GP65NB60_SVC-Code-NB60_PB01.zip

.PHONY: all clean
