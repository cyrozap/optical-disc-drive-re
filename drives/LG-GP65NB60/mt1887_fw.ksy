meta:
  id: mt1887_fw
  endian: le
  title: MT1887 Firmware Image
  license: CC0-1.0
seq:
  - id: fw_8051
    size: 0xb000
  - id: fw_arm
    size: 0xe4000
instances:
  checksum:
    pos: 0xf906a
    type: u2
