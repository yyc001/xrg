MOV AX, 15
MOV BX, 3
MOV CX, .esp

ADD DX, AX, BX
STR DX, CX
ADD CX, CX, 1

SUB DX, AX, BX
STR DX, CX
ADD CX, CX, 1

SLLV DX, AX, BX
STR DX, CX
ADD CX, CX, 1

SRLV DX, AX, BX
STR DX, CX
ADD CX, CX, 1

SLTU DX, AX, BX
STR DX, CX
ADD CX, CX, 1

AND DX, AX, BX
STR DX, CX
ADD CX, CX, 1

OR DX, AX, BX
STR DX, CX
ADD CX, CX, 1

XOR DX, AX, BX
STR DX, CX
ADD CX, CX, 1

NXOR DX, AX, BX
STR DX, CX
ADD CX, CX, 1

MUL DX, AX, BX
STR DX, CX
ADD CX, CX, 1
STR spc, CX
ADD CX, CX, 1

DIV DX, AX, BX
STR DX, CX
ADD CX, CX, 1
STR spc, CX
ADD CX, CX, 1

JNZR 0, AX

JMPR -2
0
.esp