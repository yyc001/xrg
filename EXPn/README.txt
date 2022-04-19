0->MAR //
[RAM]->MDR

-----------
0 r RAM (upline)
1 w RAM (wren)
2 r MAR
3 w MAR
4 r MDR
5 w MDR
6 r uimm
7 N/A
[8:15] r uimm
----------
r (uimm=0), w MAR	|-6--3---
r [RAM], w MDR		|--5----0
r (uimm=1), w MAR	|-6--3---
r MDR, w [RAM]		|---4--1-