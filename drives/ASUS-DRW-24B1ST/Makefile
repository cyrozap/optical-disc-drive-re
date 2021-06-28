all: 4A2M_1.00_WIN_24B1ST-i.EXE

DRW_24B1ST_VER100.zip:
	curl -O https://dlcdnets.asus.com/pub/ASUS/ODD/DVD-RW/DRW-24B1ST/DRW_24B1ST_VER100.zip

4A2M_1.00_WIN_24B1ST-i.EXE: DRW_24B1ST_VER100.zip DRW_24B1ST_VER100.zip.sha256sum
	sha256sum -c $<.sha256sum
	unzip -DD $<
	mv "4A2M_1.00_WIN_24B1ST i.EXE" $@

clean:
	rm -f DRW_24B1ST_VER100.zip 4A2M_1.00_WIN_24B1ST-i.EXE

.PHONY: all clean
