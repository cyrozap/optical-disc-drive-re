all: HLDS_RUP3_GP65NB60_BRAND_PB01-05.bin

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
	rm -f HLDS_RUP3_GP65NB60_BRAND_PB01-05.bin HDLSBIN.ZIP GP65NB60_SVC-Code-NB60_PB01.exe GP65NB60_SVC-Code-NB60_PB01.zip

.PHONY: all clean
