   1 REM any SPECTRUM
   2 REM
   3 REM Redefines 96 characters
   4 REM
   5 REM at address 31744
   6 REM
   7 REM Duration 1 minute.
   8 REM
  13 BORDER 7: PAPER 7: INK 0: CLS
  14 POKE 23607,60: REM set CHARS to normal
  15 CLEAR 31743: LET a=31744: PRINT TAB 9;"CHARACTER SET"
  20 FOR i=32 TO 127
  30 PRINT AT 21,0;CHR$ i
  40 FOR y=7 TO 0 STEP -1
  50 FOR x=6 TO 0 STEP -1
  60 IF POINT (x,y) THEN PLOT x+1,y
  70 NEXT x
  80 POKE a,PEEK (22432-256*y)
  90 LET a=a+1
 100 NEXT y
 110 NEXT i
 120 POKE 23607,123
 130 BORDER 1: PAPER 1: INK 6
 140 CLS : LIST
