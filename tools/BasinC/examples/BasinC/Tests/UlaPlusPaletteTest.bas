Check CF905390
Auto 8224

# Run-time Variables

Var a: Num = 0

# End Run-time Variables

  10 REM ulaplus Test Program
  15 PAPER 7: INK 0: CLS
  20 OUT 48955,0
  30 OUT 65339,0
  40 PAUSE 1
  50 LET a=IN 65339
  60 IF a<>0 THEN PRINT "Ula plus is NOT FOUND!"
 110 PRINT INK 2;"*Hello World"
 115 PAUSE 50
 120 OUT 48955,64: OUT 65339,1
 130 OUT 48955,15: OUT 65339,122
 131 PRINT INK 2;"*Ula Plus Enabled"'"Pink background": PAUSE 50
 132 OUT 48955,2: OUT 65339,222
 133 PRINT INK 2;"Yellow Text"
 135 PAUSE 50
 140 OUT 48955,64: OUT 65339,0
 150 PRINT INK 2;"*UlaPlus Disabled: Colours reset"
