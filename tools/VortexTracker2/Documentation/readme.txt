Vortex Tracker II v1.0 beta 24
(c)2000-2023 S.V.Bulba
Author Sergey Bulba
E-mail: svbulba@gmail.com
Support page: http://bulba.untergrund.net/

History
-------

The Vortex Tracker II idea is based on the Vortex Tracker. I and Roman
Scherbakov have started Vortex Tracker project at summer 2000, and the work was
stopped at autumn 2000 in not finished state. At August 2002 I decided to
restart work alone with new name Vortex Tracker II.

What is it?
-----------

Vortex Tracker II is a complete music editor for creating and editing music for
AY-3-8910, AY-3-8912 or YM2149F sound chips. Sound output is realized by sound
chips emulation through standard Windows digital sound devices, so, real sound
chips are not required. Vortex Tracker II uses standard Win32 functions and does
not require any additional libraries.

Vortex Tracker II can import ZX Spectrum music files (modules) of next types:

 1) Pro Tracker 3.xx (file mask is *.pt3);
 2) Pro Tracker 2.xx (*.pt2);
 3) Pro Tracker 1.xx (*.pt1);
 4) Flash Tracker (*.fls);
 5) Fast Tracker (*.ftc);
 6) Global Tracker 1.x (*.gtr);
 7) Pro Sound Creator 1.xx (*.psc);
 8) compiled  Pro Sound Maker modules (*.psm);
 9) compiled ASC Sound Master 0.xx modules (*.as0);
 10) compiled ASC Sound Master 1.xx modules (*.asc);
 11) uncompiled Sound Tracker modules (*.st1, *.ay);
 12) compiled Sound Tracker and Super Sonic modules (*.stc);
 13) recompiled Sound Tracker (*.st3);
 14) uncompiled Sound Tracker Pro modules (*.stf);
 15) compiled Sound Tracker Pro modules (*.stp);
 16) compiled SQ-Tracker modules (*.sqt);
 17) Amadeus (Fuxoft AY Language) modules (*.fxm, *.ay).

VT II detects module type only by filename extension (mask), and no any
additional checks are performed. These extensions are used in well-known player
called Ay_Emul. Any other extensions are analyzed as text files.

PT v3.7+ modules saved in TS-mode can be imported in VT II too, they are
converted to two single PT3 in two windows. Previous not documented PT v3.6 TS-
modules are imported after user prompt.

Any two tracker modules (except FXM) can be stored in one file with 16 bytes
identifier at the end of file. For text format identifier is not need. After
loading such pair VT II turns on Turbo-Sound mode and aligns both windows
horizontally.

Vortex Tracker II saves result only in one format is Pro Tracker 3.xx (*.pt3).
You can play these files in different players-emulators (the most known is
Windows and Linux emulator Ay_Emul), on real ZX Spectrum in many players
(Little Viewer, Quick Commander, Real Commander, BestView, Pusher, ZXAmp, The
Viewer and so on) or by built-in playing routines. Also you can include
YM-sound into your PC-programs (see Ay_Emul sources, YM-Engine or SquareTone at
http://bulba.untergrund.net/).

During editing you can save work versions of module in text format. It allows
to save all temporary not used ornaments, samples and patterns. Also, text
format is easy editable in any text editor. Of course, text format is only
one chance to save your music, if PT3 saving is not available due size
limitations (65536 bytes).

In Turbo-Sound mode during saving one of module second module is saved to the
end of file too.

In fact, Vortex Tracker II is PC version of ZX Spectrum Pro Tracker 3.xx.
The most compatible version is Pro Tracker v3.6x-3.7x of Alone Coder (a.k.a.
Dima Bystrov). Vortex Tracker II is fully compatible with any Pro Tracker v3.5x
in "ProTracker 3.5" mode.

All supported formats are converted to Pro Tracker 3 compatible format,
therefore some information can be lost, because of ZX music formats are very
badly compatible between each other. More information about converting you can
see in 'Tracker limitations.rus.txt' file.

New 3xxx interpretation is supported in last Pro Tracker 3 versions from Alone
Coder (v3.6 and higher).

During editing total time length and current time position are calculated
automatically (for demomakers).

Note: new 3xxx interpretation changes behavior of ASC modules import also.

This version has next new features:

05/10/2023:

1. Fixed another bug of manually selecting the highlight step on a newly
   created (i.e. empty and uninitialized) pattern: when trying to enter a zero
   step, a failure occurred.
2. The "Decimal numbering" and "Decimal noise" buttons have been added above
   the corresponding tracks to switch to the decimal numbering of track lines
   and display the noise period at any time (a similar idea is implemented in
   Ivan Pirog's Vortex Tracker v2.6).
3. Two parameters for new windows have been added to the options window for the
   same purpose: "Decimal noise period" and "Decimal line numbering".
4. Font styles are now ignored (except for bold).
5. The cursor width could be displayed incorrectly in the tracks during Undo
   (when alternating changes in notes and parameters). Fixed.

05/11/2023:

6. The "Envelope as note" button has been added above the envelope track. The
   option has been asked to be implemented for a long time (TAD asked me about
   it for the first time many years ago), but I put it on hold until I saw the
   implementation in Ivan Pirog's Vortex Tracker II v2.6 and wanted to do it a
   little differently: the envelope period is replaced by a note only if a
   cyclic envelope type is specified in one of the channels; the octave of a
   note depends not only on the envelope period, but also on its type; if the
   envelope type is specified in several channels, the type from the largest by
   channel number is taken (this is how all the players I know are arranged).

05/12/2023:

7. Octave 0 has been added to display the envelope periods up to FF and C-0,
   everything below is displayed traditionally in HEX.
8. Another parameter has been added to the Options window for new windows,
   "Envelope as note", which allows you to make the corresponding displaying
   the envelope period mode the default mode.
9. Editing of the envelope period track in the pattern has been modified for
   the "Envelope as note" mode: a wide cursor; input with note keys;
   calculation and substitution of a note in the appropriate channel (if
   AutoEnv is enabled); clearing the selection and cutting/copying it to the
   clipboard have been rewritten so that all four digits of the envelope period
   are captured, if in their place a note is displayed; switching the "Envelope
   as note" mode corrects the cursor position and selection boundaries in the
   area of the envelope period display. To enter notes from octave 0, turn on
   octave 1 and use the standard keyboard shortcut to enter a note an octave
   lower (Ctrl+Shift+NoteKey).

05/13/2023:

10.Now you can insert notes from any channel from the clipboard into the
   envelope period track. If the envelope type is specified in one of the
   channels when inserting the target pattern in the corresponding line, it
   will be taken into account when recalculating from the note number to the
   envelope period, otherwise the calculation is performed as for a type 8
   envelope (the same result as type C).
11.Bug fixed: when pasting from the clipboard into a newly created (i.e. empty
   and uninitialized) pattern, a crash occurred.
12.The envelope periods copied to the clipboard (in any display mode) can now
   be inserted into the note tracks of any of the channels. The conversion of
   the period to the note number is performed as for an envelope of type 8/C.
   If these periods were used with the A/E type, you will need to manually
   transpose the result an octave lower. If the periods are copied in the
   traditional display mode (HEX), you need to capture all four digits before
   copying, only in this case the insertion algorithm will group them as one
   whole if the insertion is made in a track with notes.

05/14/2023:

13.A table number selection for new modules has been added to the Options
   window.
14.Another idea from Ivan Pirog's Vortex Tracker II v2.6 has been implemented:
   when changing the note table in the module, the envelope periods can be
   recalculated. You can disable this feature in the Options window. A window
   appears with a request to confirm the operation before the recalculation,
   because it cannot be rollbacked via Undo.
15.Transposition in envelope period tracks is now done according to the
   envelope periods to notes conversion table, and not to the formula (the idea
   is taken from Vortex Tracker II v2.6). For this reason, those periods that
   are not recognized as notes (outside of the note range or indicating a
   non-cyclic envelope type) are no longer transposed.
16.Added tooltips for the selected tone table number, indicating which clock
   frequency of the music chip they are suitable for.
17.The Close All to close all windows and Find Module to search for a window by
   a fragment of the file name, title or author's name items have been added in
   the Windows menu (thanks to Alexander Boolba for the icon and code).

05/16/2023:

18.The standard Cascade Windows method has been replaced with the code provided
   by Alexander Boolba. When cascading, windows (including TS pairs) are
   positioned better now.
19.If one of the TS-pair windows becomes active, the second one is also brought
   to the foreground (thanks to Alexander Boolba for the code).
20.New windows positioning is now performed by Alexander Boolba's Cascade
   Windows algorithm.

05/17/2023:

21.The standard Tile Vertically and Tile Horizontally methods have been
   replaced with code provided by Alexander Boolba.

Short manual
------------

Next keys are used.

 Pattern editor keys
 ~~~~~~~~~~~~~~~~~~~

1. In a note cell

1.1. NoteKeys:

                          Q 2 W 3 E R 5 T 6 Y 7 U I 9 O 0 P [ = ]
  Z S X D C V G B H N J M , L . ; /

  | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
  | C#| D#| | F#| G#| A#| | C#| D#| | F#| G#| A#| | C#| D#| | F#|
  C   D   E F   G   A   B C   D   E F   G   A   B C   D   E F   G

So fortepiano keys are emulated with range more than two octaves.

- If cursor in a note cell of track column, use numpad keys from 1 to 8 to
 (only when NumLock is on), key "A" for (R--) and key "K"  (---).

1.2. Shift+NoteKeys - input note one octave higher.

1.3. Shift+Ctrl+NoteKeys - input note one octave lower.

1.4. A - for sound off in channel command (R--).

1.5. K - for delete note (---).

1.6. From 1 to 8 at NumPad - choose current octave number.

During inputting numbers from NumPad NumLock must be turned on.

2. Pattern navigation (cursor control)

2.1. Up, Down, Left, Right - move cursor in four directions.

2.2. PageUp, PageDown - move cursor to page up or down.

2.3. Home, End - move cursor to begin or end of line.

2.4. Ctrl+Right, Ctrl+Left - quick cursor moving among columns.

2.5. Ctrl+PageUp, Ctrl+PageDown - move cursor to top or bottom of column.

2.6. Ctrl+Home, Ctrl+End - move to top of first or bottom of last column.

2.7. Mouse clicks - move cursor to desired cell.

2.8. Mouse wheel - scroll pattern up/down.

3. Pattern's area selection

3.1. Shift+cursor control keys (i.2.) - select rectangular area of pattern.

3.2. Ctrl+A, Ctrl+5 on NumPad - select all pattern.

3.3. Moving mouse with pushed left button.

3.4. Shift+mouse click - select from cursor to desired cell.

3.5. Shift+mouse wheel - not reset/add to selection.

4. Jumps from edit pattern to other objects

4.1. Tab - jump from one window control to other in predefined order.

4.2. Shift+Tab - same in reverse order.

4.3. ` (back apostrophe, usually over Tab key) - quick switch between pattern
and position list editors.

5. Deleting

5.1. BackSpace - delete current track line (with moving).
                                                          
5.2. Ctrl+BackSpace, Ctrl+Y - delete current pattern line (with moving).

5.3. Delete - clear selection's values or value at cursor position.

5.4. Ctrl+Delete - clear pattern line values.

5.5. Numpad / - delete each 2nd pattern line with moving and decreasing pattern
     size.

6. Inserting empty lines

6.1. Insert - insert empty track line (with moving).

6.2. Ctrl+I - insert empty pattern line (with moving).

6.3. Numpad * - double pattern size with inserting empty pattern lines between
     old lines.

7. Working with selection

7.1. Ctrl+C, Ctrl+Insert - copy selection to clipboard.

7.2. Ctrl+X, Shift+Delete - same with clearing selection values.

7.3. Ctrl+V, Shift+Insert - inserting from clipboard (to right and to down from
     cursor or from upper left corner of selection). In case of selection is
     defined, insertion not exceeds its bounds.

7.4. Ctrl+Alt+V - same as usual inserting from clipboard, but without replacing
     non-empty values with empty ones (i.e. merging).

7.5. Numpad + and Numpad - - transpose 1 semitone up and down.

7.6. Ctrl+Numpad + and Ctrl+Numpad - - transpose 1 octave up and down.

8. Test playing of pattern's part

8.1. Any pushed key during inputting data - play current line.

8.2. Pushed Enter key - play pattern from current cursor position until key
is pushed. If any looping is on, pattern will be playing cyclically,

9. Other

9.1. 0 on NumPad - on/off Auto Envelope.

9.2. Space - on/off Auto Step.

9.3. Shift+Backspace - if Auto Step is on do step backward.

Right mouse button can call pop-up menu, which duplicates some key combinations
(useful if you are using keyboard without Numpad, like in notebooks).

 Common keys
 ~~~~~~~~~~~

1. Play controls

1.1. F5 - play module from current position.

1.2. F6 - play module from start.

1.3. F7 - play current pattern from current line.

1.4. F8 - play current pattern from start.

1.5. Esc - stop playing and go to edit pattern; also use to free sound device.

1.6. Ctrl+L - module and pattern loop playing on/off.

1.7. Ctrl+Alt+L - loop playing among all opened modules on/off. If only one
module is opened or pattern is playing, it works as usual loop.

2. Sound chip emulation

2.1. Ctrl+Alt+C - toggle chip type (AY-3-8910/12 or YM2149F).

2.2. Ctrl+Alt+A - toggle channel allocation (Mono, ABC, ACB and BAC, all other
can be selected in 'Options' dialog).

3. Editing

3.1. Ctrl+E - toggle autoenvelope mode to autocalculating envelope period by its
type and current note.

3.2. Ctrl+R - toggle autostep (edit spacing).

3.3. Ctrl+T - call Track Manager dialog.

3.4. Ctrl+Alt+T - call Global Transposition dialog.

3.5. Up/Down in the text fields with arrows to increase or decrease the value
by one.

3.6. PageUp/PageDown in the pattern length text field to increase or decrease
the value by the amount of the highlighting step.

4. Standard keys

4.1. Alt+F4 - close Vortex Tracker II.

4.2. Ctrl+F4 - close active window with module.

4.3. Ctrl+F6 - cyclic choosing of opened modules.

4.4. Ctrl+O - call open dialog.

4.5. Ctrl+S - save module.

4.6. Tab, Shift+Tab - cyclical jumps between window controls (forward and
backward).

4.7. Alt+BackSpace - undo last change.

4.8. Alt+Enter - redo last change.

 Positions list editor keys
 ~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ` - jump to/from pattern editor.

2. Left, Right or left mouse button - select position (during playing selected
position will restart playing).

3. Right mouse button - select position and call popup menu.

4. L - set loop position.

5. From 0 to 9 - enter pattern number for selected position.

6. Del - delete position with moving.

7. Ins - insert position with moving.

 The sample editor keys
 ~~~~~~~~~~~~~~~~~~~~~~

Up, Down, Left, Right, PageUp, PageDown, Home, End, Ctrl+Right, Ctrl+Left,
Ctrl+PageUp, Ctrl+PageDown, Ctrl+Home, Ctrl+End for navigation.

Shift+navigation keys described above for area selection.

In any position of editing sample:

T - toggle on/off tone mask
N - toggle on/off noise mask
M - toggle on/off envelope mask

In 'TNE' columns:
Space - toggle on/off corresponding mask

In any '+' and '-' columns:
Space - toggle sign
Shift+'=', '=', Numpad '+' - change sign to '+'
'-', Numpad '-' - change sign to '-'
Shift+6 ('^') - turning on accumulation in corresponding column '^'
Shift+'-' ('_') - turning off accumulation in corresponding column '_'
0-9,A-F - enter hexadecimal numbers

In any '^' and '_' columns:
Space - on/off accumulation
Shift+6 ('^') - turning on accumulation '^'
Shift+'-' ('_') - turning off accumulation '_'
0-9,A-F - enter hexadecimal numbers

In last column (volume control) '+', '-' and '_':
Space - toggle three variants
Shift+'-' ('_') - don't change sample volume '_'
'-',  Numpad '-' - decrease sample volume by one '-'
'+',  Numpad '+' - increase sample volume by one '+'
0-9,A-F - enter hexadecimal numbers

In the number fields:
0-9,A-F - enter hexadecimal numbers
Space - change sign, in amplitude column - volume control
Shift+'=', '=', Numpad '+' - change sign to '+'
'-', Numpad '-' - change sign to '-'
Shift+6 ('^') - turning on accumulation '^'
Shift+'-' ('_') - turning off accumulation '_'

Any non-digital key or mouse clicking reset number inputting counter.

Right mouse clicking in amplitude visualization field ('*' symbols) to choose
corresponding amplitude.

Moving mouse with clicked right button in amplitude visualization field to
draw amplitude.

Middle mouse click in some sample cells to toggle corresponding value.

Right-clicking on the selection opens a pop-up menu.

Shift+mouse click to select area from cursor to click point.

Ctrl+C/Ctrl+X to copy/cut the selected fragment to the clipboard.

Ctrl+V to paste from the clipboard from the cursor position or inside the
selection. Heterogeneous data can be inserted, for example, tone deviation
signs or values can be inserted into noise/envelope deviation signs or values.

Delete to clear the selected area or what is under the cursor.

 The ornament editor keys
 ~~~~~~~~~~~~~~~~~~~~~~~~

Up, Down, Left, Right, PageUp, PageDown, Home, End, Ctrl+PageUp, Ctrl+PageDown,
Ctrl+Home, Ctrl+End for navigation.

Shift+navigation keys described above for area selection.

0-9 - input decimal numbers

Space - toggle number sign

Shift+'=', Numpad '+' - set '+' sign

'-', Numpad '-' - set '-' sign

Use middle mouse click to toggle sign of corresponding value.

Right-clicking on the selection opens a pop-up menu.

Shift+mouse click to select area from cursor to click point.

Ctrl+C/Ctrl+X to copy/cut the selected fragment to the clipboard.

Ctrl+V to paste from the clipboard from the cursor position or inside the
selection.

Delete to clear the selected area or what is under the cursor.

 Plugin for editing an ornament
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If orgen.exe file is available, you can click the OrGen button to launch the 
orgen plugin by Shiru Otaku. Use the plugin to edit ornaments in an alternative
way.

 Sample and ornament test fields
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigation and editing same as in patterns editor. Selecting, copying, pasting
from the clipboard also works (you can copy data from the pattern to the test
line and vice versa).

 Other elements to edit
 ~~~~~~~~~~~~~~~~~~~~~~

Title and author strings maximum length is 32 chars.

Highlight step for pattern lines can be adjusted in patterns sheet. If AutoHlt
is on, step is autoselected from 3, 4 and 5 depending of pattern length. The
size of the highlighting step is also used in the text field of the pattern
length editor with the PageUp and PageDown keys.

Save command available only after starting editing of song.

 Notes on the capabilities of PT3 editors of different versions
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can load VT II modules into ZX Spectrum Pro Tracker 3.69x-3.7x. It can load
modules with VT II header and with *.pt3 file extension.

For playing module by standard ZX Spectrum playing routine don't select song
speed smaller than 2 (3 for old players), or better use VT II built-in player
without such limitations.

Header types
------------

Current version can save three header types in PT3-file.

1) 'Vortex Tracker II 1.0 module: '

This header means, that module can contain all VT II abilities, including new
3xxx interpretation. However, module can be played with old PT3-players without
any problems in most cases.

2) 'ProTracker 3.6 compilation of '

This header means same abilities, as previous one. It need for some players,
which require old header style.

3) 'ProTracker 3.7 compilation of '

In addition to PT 3.6 abilities, module can contain glissando commands 1.xx and
2.xx (timedelta=0). In this case glissando not works as usually, instead single
tone frequency changing by xx down or up is performed.

4) 'ProTracker 3.5 compilation of '

This header means, that module must be played with old 3xxx command
interpretation and 1.xx and 2.xx special commands must be ignored.

AutoStep using
--------------
During editing tracks step of autoscrolling can be set. It works after the most
typical operations: typing note, sample, numbers, inserting/deleting/clearing
lines and so on. Tracks can be autoscrolled up (positive step) and down
(negative step). To fast switch autostep option use Space or Ctrl+R.

You can use this feature for unusual tasks, like inserting same data from
clipboard with given step, or fast changing patterns size in 2 times (both
increasing and decreasing). In last case just set step to 2 or 1 and use Ctrl+I
or Ctrl+BackSpace several times (for last better use Compress/Expand commands of
popup menu).

Sometimes user does not remember that AutoStep is on, so, he can press
Shift+Backspace to do step backward.

Turbo-Sound mode
----------------
From the end of 90s some people tried to popularize standards of two sound chips
connection to ZX Spectrum. Known schemes are Quadro-AY, Turbo-AY and
Turbo-Sound. One of way to use it is to play two different modules
simultaneously (each through own chip). Vortex Tracker II allows playing any two
opened modules simultaneously. Active window module sounds through the first
sound chip, and module selected in list of opened modules through the second
chip (call list by pushing corresponding button of module window). By default,
second chip is off ("2nd soundchip is disabled" button label appears).

For more usability VT II synchronizes tracks of two modules in both play and
edit tracks modes (including cursors position), activates 2nd window after
reaching tracks editor cursor right or left position, during saving any of
TS-pair module, 2nd is added to result file (firstly created saved first in the
file), during loading TS-modules (including special format from PT v3.6+)
creates TS-pair and aligns it horizontally. Also, the resize/close of any
window in pair leads to same actions in second one.

Examples of playing on ZX can be found in ZX-magazine InfoGuide #8.

During exporting to ZX in TS-mode used special TS-player for ZX Spectrum.

Files->Options... menu
----------------------

Calls the Options window (you can also call by clicking on the corresponding
button on the panel). All settings are applied immediately, but at any time you
can click the Cancel button (or just close the window) and return to the
settings that were before the Options window was called. In order for the
settings to be remembered, click OK.

'Design' tab sheet

By clicking on the 'Design Items' fields, you can customize the fonts and
colors of the edited pattern, sample, ornament or their testing lines items.
The font selection dialog displays only monospaced fonts such as Courier,
Courier New, Fyxedsys, Lucida Console. Due to the fact that all characters in
such fonts have the same size in width, it becomes possible to fast print
tracks and to calculate coordinates for displaying the cursor and selection.

Here you can also configure the initial ones: the number of visible lines of
the track (from 3 to 64), the number of the note table, the decimal/hexadecimal
system for displaying line numbers and noise periods columns in the pattern, as
well as the mode for displaying the envelope period as notes. In the future,
these parameters can be changed individually for each window, while when the
window size changes, the number of lines in tracks, samples and ornaments is
synchronously recalculated.

'Chip emulation' tab sheet

Choose chip type, chip and interrupt frequency, channels allocation (both
hearable and visual), and one of resample algorithm. Some changes can be heard
after time shown in bottom of tab sheet. Some musicians use tricks, which can
sound rightly only if FIR-filter is selected (checked by default). Of course,
FIR-filter requires more processor time. So, if your system cannot produce
solid sound, select Averager or decrease bitrate or sample rate at 'Digital
Sound' tabsheet. In Turbo-Sound mode used identical setting for both chips.

'Compatibility' tab sheet

These are global compatibility options. If you need to adjust only current
module, see corresponding tab sheet on its window.

 Features level

 - Pro Tracker 3.5 - old behavior of 3xxx command. Also ASC modules will be
       imported for playing with old PT3 players.
 - Vortex Tracker II (PT 3.6) - new 3xxx command interpretation. It affects to
       playing and ASC modules import.
 - Pro Tracker 3.7 - allows using of 1.xx and 2.xx special commands.
 - Try detect - allow VT to detect it. For PT3 are used header analyzing (see
       rules above). For PT2 is used 'Pro Tracker 3.5'. For all other - 'Vortex
       Tracker II (PT 3.6)'.

 Save with header

 You can recommend to VT II save one of header type. Anyway, VT II uses known
 rules (see 'Header types').

'Digital sound' tab sheet

This is wave out sound options. All options are not available during playing. To
stop playing press corresponding button of the sheet.

 Sample rate

  Samples frequency, more value for more quality. If some frequency is not
  supported by sound card can be error messages or sound quality will be worse.

 Bit rate

  Sample size, more value for more quality.

 Channels

  Mono or Stereo.

 Device

  'Wave mapper' as default.

 Buffers

  Buffer size and number of buffers. Try to find optimal values for you system.
  Smaller buffer size for quicker reaction. More buffers for stable sound. Total
  length of buffers are calculated at low side of group.

'Other' tab sheet

 Application priority

  Select normal or high priority.

 Recaculate envelope period on note table change

  This option allows automatic envelope periods recalculation when changing the
  note table number. Since the operation is not adding into the Undo list, a
  corresponding request is output before it is executed. Envelopes are
  recalculated according to the converting tables of periods to notes and back
  (they are also used in the displaying envelope periods as notes mode), so if
  the period is greater than #00FF or lower than C-0, or is not used with a
  cyclic envelope type (8, A, C or E), it is not recalculated.
  
Track manager
-------------

To call press Ctrl+T or choose corresponding Edit menu option. You can copy
any part of any pattern to any place of any pattern.

In Location 1 and Location 2 group adjust pattern number, first line number and
channel number. In Area group set number of lines, and if you need check noise
and envelope tracks.

To copy one location to another simply press corresponding button in Copy group.
Also you can move or swap locations (see Move and Swap groups).

Also you can transpose any location to desired number of semitones (see
Transposition group). Positive values for up and negative for down. If you
check Envelope track (Area group), it'll be transposed too.

Global Transposition
--------------------

To call press Ctrl+Alt+T or choose corresponding Edit menu option. You can
transpose one or more tracks of whole module or of selected pattern. This
dialog allows avoid multiple using of Tracks manager. Adjusting and using same
as in Tracks manager.

Menu Files->Save and Files->Save as...
--------------------------------------

In appeared save dialog select in dropdown list file type for saving module:
either work text format (TXT) or Pro Tracker 3 (PT3) for final compilation.
During saving PT3 format, VT II removes all not used samples, ornaments and
patterns.

Menu Files->Exports->Save in SNDH (Atari ST)
--------------------------------------------

Saving in SNDH format for playing on Atari ST (or in SNDH-players and emulators
of Atari ST). There is universal MC68000 player used in SNDH, it supports all
note and volume tables (starting from PT 3.3), PT3 module version is analyzed
during initialization. Player is based on Ay_Emul procedures, volume and note
tables are packed by Ivan Roshin's method. SNDHs are not packed by PACKICE in
this version. Player size is about 9 Kb; start address is not fixed. Before
saving 'Year of creation' prompt are shown, you can ignore it if it not need.

Menu Files->Exports->Save with ZX Spectrum player
-------------------------------------------------

Saving with ZX Spectrum player. Supported formats: HOBETA with player ($c),
HOBETA without player ($m), .AY of EMUL subtype, SCL and TAP. .AY-format not
allows using 0 address. Player can be adjusted: you can disable looping of
module, check 'Disable loop' for that. In SCL and TAP formats, player and module
both are saved separately (in two different files). It is better than HOBETA,
because variables area between player and module is not saved. Player features
and instructions can be found in ZXPlayer.txt file. Source text of player can be
found in archive with VTII sources, and also at http://bulba.untergrund.net/

Thanks to
---------

- Roman Scherbakov (a.k.a. V_Soft) for idea and picture.
- Konstantin Yeliseyev (a.k.a. Hacker KAY) for AY and YM level tables.
- Dmitry Bystrov (a.k.a. Alone Coder) for information about Pro Tracker 3.xx.
- Roman Petrov (a.k.a. Megus) for ideas about ideal AY tracker.
- Macros for testing, test files, wishes about interface and for support.
- Shiru Otaku for plug-in, testing, wishes and bug-reports.
- Polaris for wishes and test modules.
- Black Groove (a.k.a. Key-Jee) for bug-reports, wishes and test modules.
- Ilya Abrosimov (a.k.a. EA) for bug-reports and wishes.
- Pavel A. Sukhodolsky for help and formats discussion.
- Asi for bugreports and wishes.
- Denis Seleznev for icon pictures.
- Spectre for help in debugging and wishes about ZX PT3-player.
- Ivan Roshin for help in writing new ZX PT3-player.
- Jecktor for adapting PT3-player sources to XAS.
- HalfElf for using in xLook Far Manager plug-in.
- Karbofos for testing, suggestions and test modules.
- Ch41ns4w for wishes about TS-mode and about design.
- Znahar for another branch of VT II with good ideas.
- TAD for suggestions, bug-reports and test modules.
- MMCM for suggestions.
- Nik-O for suggestions.
- To Ivan Pirog and the Vortex Tracker II v2.6 team for ideas.
- To Alexander Boolba for closing windows icon, some functions code and ideas.

Special thanks to people who wrote or write music in Vortex Tracker II:
4Mat
AER
Akasaka
Alex Rostov
Alexander Boolba
Alone Coder
And
ant1
Aprisobal
Asi
Astamur Panov
AZ
Bey Elder
Beyker
Biozoom
Black Fox
Bloobop
Bonysoft
buzzkej
Byteman
casecoma
Cat-Man
Ch41ns4w
Chip Champion
Cj Echo
Crazy Pixel
Creator
Darkman007
DDp
dead8088
Deetsay
Destr
Dippy
Dj Denson
Dj Kot
Dj Max
DoctorGentleman
EA
Elfh
Ellvis
emook
Esau
Factor6
Firestarter
Frank Triggs
Fubukimaru
funute
Garvalf
Gasman
Gibson
gotoandplay
gyms
isihlabathi
Jangler
Jass
Jerrs
Johnny McGibbitts
Joker
JosSs
Joyrex
jrlepage
Jumperror
Justinas
Kakos_nonos
Karbofos
kas29
Key-Jee
kfaraday
Klim
Kriss
kubikami
Kulor
KUVO
Kyv
Lamer Pinky
Lee du-Caine aka dC Audio
LiSU
m9m
MAD_DEL
MadMax of KNA
Makinavaja
mborik
Megus
Mic of MPS
Misha Pertsovsky
Mmcm
Mofobaru
Molodcov Alexander
MovieMovies1
neppie
nikhotmsk
Nik-O
Nooly
NVitia
OldFartGamer
Orson
Pak-Zer0
Pator
petet
Pigu
PSB
Quiet
rainwarrior
REAKTIVZ
Riskej
Robyn
Rolemusic
Rubedo
ruguevara
Ryurik
Samanasuke
Sarek
Sayk
Scalesmann
Sentinel
Sharik
Shiru Otaku
Siril
Splinter
Stiffler
Striker of Megasoft
Sultan Paraiso
TAD
tayle
th4 D34D
Tobikomi
Tosha
TristEndo
usagi
V0yager
Vadimatorik
Vedem
Voxel
Wally
wbc
Yerzmyey
z00m
Z23
Ziutek
ZJ Alex Clap
Zlew
Znahar
ZoundMakkr
zxastafiew
and you ;)

Distribution
------------

Vortex Tracker II is free program. There are two kind of original distribution:
binary (VT.exe with documentation) and sources (source files as Lazarus project
with documentation). You can use and distribute sources freely, simply credit me
somewhere in your projects, where you include all or part of the sources and
(or) my algorithms.

Sergey Bulba

24 of August 2002 - 18 of May 2023
