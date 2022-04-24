  MOV AX, .ad1
  LD  BX, AX
  ADDU BX, BX, AX
  MOV CX, 0
.loop
  ADDU AX, AX, 1
  LD  DX, AX
  ADDU CX, CX, DX
  NXOR DX, AX, BX
  JZ  DX, .loop
  STR .ad2, CX
  HALT
.ad1
5
1
3
5
6
8
.ad2