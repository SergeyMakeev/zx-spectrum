 100 RANDOMIZE : PAPER 7: INK 0: BORDER 7: FLASH 0: BRIGHT 0: OVER 0: INVERSE 0
 110 DATA 0,0,24,126,189,36,0,0,0,0,153,126,60,36,0,0
 120 FOR a=0 TO 15: READ b: POKE a+USR CHR$ 144,b: NEXT a
 130 LET s=50: LET x=15
 200 FOR f=144 TO 145: LET s=s-1: PRINT AT 0,x; INK 1;CHR$ f
 210 IF INKEY$ ="o" AND x>0 THEN LET x=x-1
 220 IF INKEY$ ="p" AND x<31 THEN LET x=x+1
 230 PRINT INK 2;AT 19,31*RND ;"^";AT 19,31*RND ;"^"
 240 IF RND <.3 THEN PRINT INK 4;AT 19,31*RND ;"."
 250 POKE 23692,0: PRINT ',,,s: IF s<=0 THEN GO TO 300
 260 LET p$=SCREEN$ (0,x): IF p$="^" THEN GO TO 300
 270 IF p$="." THEN LET s=s+20: BEEP .05,30
 280 NEXT f
 290 GO TO 200
 300 FOR a=0 TO 19: BEEP .05,20-a
 310 PRINT INK 1;AT a,x;" ";AT a+1,x;CHR$ 145
 320 NEXT a
 330 BEEP .1,-40
