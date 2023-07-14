Check 1C5D2B3C
Auto 8224

# Run-time Variables

Var a: Num = 103

# End Run-time Variables

 100 POKE 23560,0
 110 LET a=PEEK 23560: PRINT AT 0,0;a;"  "
 120 IF (a<8 OR a>11) AND a<>13 THEN GO TO 110
