Check 2E745351
Auto 8224

# Run-time Variables

Var sy: Num = 8
Var sx: Num = 8
Var f: NumFOR = 10, 9, 1, 510, 2
Var y: NumFOR = 8, 9, 1, 50, 3
Var x: NumFOR = 1, 9, 1, 50, 4
Var g: NumFOR = 10, 9, 1, 510, 3
Var s$: Str = "788796"
Var n$: Str = "197988"
Var y$: Str = "o"
Var x$: Str = " "
Var a$: StrArray(9, 9) = "                                        #        #        #    o   #  *     #    "
Var b$: StrArray(9, 9, 2) = "21222324252627282931323334353637383941424344454647484951525354444546474861626364# 4647484971727374# 5657585981828384# 66676869o 818283# 767778  81828384# 86      "

# End Run-time Variables

  10 REM pathfinder with Dykstra algorithm
  20 DIM a$(9,9): REM the field
  30 FOR f=5 TO 9: LET a$(f)="    #    ": NEXT f
  31 REM LET a$(5)=a$(1)
  35 REM line 30 and 31 is make field, second test remove REM from 31
  40 LET a$(8,1)="o": REM the end
  49 REM now set all obtacles. End is also obstacle
  50 DIM b$(9,9,2): FOR y=1 TO 9: FOR x=1 TO 9: LET b$(y,x)=a$(y,x): NEXT x: NEXT y
  57 REM Now set start
  58 LET sy=8: LET sx=8
  60 LET a$(sy,sx)="*"
  90 REM display field
 100 FOR f=1 TO 9: PRINT PAPER 6;AT f,1;a$(f): NEXT f
 190 REM Work backworks, so start at end
 200 LET s$="81": REM coordinates for end
 210 LET n$="": REM All knots reached from this knot
 220 LET y=VAL s$(1)
 230 LET x=VAL s$(2)
 235 IF x=1 THEN GO TO 245
 236 REM Handle left
 240 LET x=x-1: IF b$(y,x)="  " THEN LET b$(y,x)=s$( TO 2): LET n$=n$+STR$ y+STR$ x: IF (sy=y) AND (sx=x) THEN GO TO 390
 241 LET x=x+1
 245 IF x=9 THEN GO TO 255
 246 REM Handle right
 250 LET x=x+1: IF b$(y,x)="  " THEN LET b$(y,x)=s$( TO 2): LET n$=n$+STR$ y+STR$ x: IF (sy=y) AND (sx=x) THEN GO TO 390
 251 LET x=x-1
 255 IF y=1 THEN GO TO 265
 256 REM Handle up
 260 LET y=y-1: IF b$(y,x)="  " THEN LET b$(y,x)=s$( TO 2): LET n$=n$+STR$ y+STR$ x: IF (sy=y) AND (sx=x) THEN GO TO 390
 261 LET y=y+1
 265 IF y=9 THEN GO TO 275
 266 REM Handle down
 270 LET y=y+1: IF b$(y,x)="  " THEN LET b$(y,x)=s$( TO 2): LET n$=n$+STR$ y+STR$ x: IF (sy=y) AND (sx=x) THEN GO TO 390
 271 LET y=y-1
 280 LET s$=s$(3 TO ): REM Fetch next knot
 290 IF s$<>"" THEN GO TO 220
 300 LET s$=n$: IF s$<>"" THEN GO TO 210: REM No end while knots are reached
 390 REM Show shortest route
 400 LET y=sy: LET x=sx: REM Startcoordinates
 410 PRINT AT y,x;"."
 420 LET y$=b$(y,x,1): LET x$=b$(y,x,2)
 430 IF x$<>" " THEN LET y=VAL y$: LET x=VAL x$: GO TO 410
 500 PRINT AT 10,0;
 510 FOR f=1 TO 9: FOR g=1 TO 9: PRINT AT f+11,g;b$(f,g,1): NEXT g: NEXT f
