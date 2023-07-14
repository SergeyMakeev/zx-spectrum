
Open BasinC and then save to TAP  
Use BasinC built in TAP editor to make it autostart from LINE 10  


https://chuntey.wordpress.com/2013/10/02/how-to-write-zx-spectrum-games-chapter-18/  

### Typing hints on Spectrum48  
```
10 CLEAR 24575
20 LOAD "" SCREEN$
25 POKE 23739,111
30 LOAD "" CODE 32768
40 RANDOMIZE USR 32768
```

X = 'Clear'  
J = 'Load'  
Ctrl+P = '"'  
Ctrl+Shift = "E" +  Ctrl+K = 'Screen$'  
O = 'Poke'  
Ctrl+Shift = "E" + I = 'Code'  
T = 'Randomize'  
Ctrl+Shift = "E" + I = 'Usr'  
S = 'Save'  
Ctrl+Shift = "E" +  Ctrl+3 = 'Line'  

### How to save
```
SAVE "loader" LINE 10
```
