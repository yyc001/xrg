
; 示例程序 1
; 下面的程序对若干个数字求和
; ad1 存放数字的个数，表示接下来有[ad1]个数需要求和
; 计算的结果保存在ad2中

  MOV AX, .ad1
  LD  BX, AX
  ADD BX, BX, AX
  MOV CX, 0
.loop
  ADD AX, AX, 1
  LD  DX, AX
  ADD CX, CX, DX
  XOR DX, AX, BX
  JNZ  DX, .loop
  STR  CX, .ad2
  HALT
.ad1
3
101
102
103
104
105
.ad2