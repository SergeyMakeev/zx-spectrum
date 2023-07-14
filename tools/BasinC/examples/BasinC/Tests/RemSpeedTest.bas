Check 41F054C8
Auto 8224

# Run-time Variables

Var x: NumFOR = 256, 255, 1, 3332, 2

# End Run-time Variables

   1 REM slow
   2 FOR x=0 TO 255
   3 PLOT x,10
   4 NEXT x
  10 REM speed 1
  20 FOR x=0 TO 255
  30 PLOT x,10
  40 NEXT x
  50 REM speed 20
 120 FOR x=0 TO 255
 130 PLOT x,30
 140 NEXT x
 150 REM speed 40
1120 FOR x=0 TO 255
1130 PLOT x,60
1140 NEXT x
2210 REM fast
2220 FOR x=0 TO 255
2230 PLOT x,90
2240 NEXT x
3331 REM slow
3332 FOR x=0 TO 255
3333 PLOT x,130
3334 NEXT x
