Check F57CA6CA
Auto 8224

# Run-time Variables

Var x: Num = 91
Var y: Num = 199
Var x1: Num = 238
Var y1: Num = 157
Var button: Num = 255

# End Run-time Variables

   1 LET x1=10: LET bx=10: LET by=10: LET y1=10
  10 LET button=IN 64223: LET x=IN 64479: LET y=IN 65503
  20 IF button<>255 THEN PLOT x1,y1
  50 IF (x1=x AND y1=y) OR x>244 OR (y>170 OR y<10) THEN GO TO 10
  55 PLOT OVER 1;x1,y1: DRAW 5,-5
  60 PLOT x,y: DRAW 5,-5
  70 LET x1=x: LET y1=y
 100 GO TO 10
