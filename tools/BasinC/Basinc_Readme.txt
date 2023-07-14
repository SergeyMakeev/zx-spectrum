BASINÇ Version 1.792 by Arda "ref" Erdikmen

This is not BASin. BasinC is a fork of highly successful Basin Project by Paul Dunn et al. 
BasinC is based on Basin's R14 source code and working parts of R15 source.

USAGE/INSTALLATION:
No installer. Unzip all files whereever you want, and execute Basinc.exe. Exe file should have read/write permission to it's folder to save settings.

UPGRADING FROM AND OLDER INSTALLATION
If you are upgrading from pre-1.7 version it's recommended to start fresh. New basinc requires autoback folder and "basinC.bin" file to run properly.

You may contact the author on ardarda@gmail.com - this project is unaffiliated with the SPIN team, and therefore the other members will be unable to help you a great deal.

Disclaimer: Z80 emulation may not be accurate for certain tasks. Files (saved with/loaded by)* BASinc may not be compatible with other emulators. BASin may format your hard drive.

* Delete as appropriate.


Recent // history & todo:

// 1.79.2 (19.05.2022)
// Added - Basin Update Check (disabled by default, enable in Options)

// 1.79.1 (19.05.2022)
// Added - BasinC Snippets
// Changed - SimpleCon behaviour. Not port 1515 commands sets the byte *then* increment the index. Port 1259,0 feeds the line to the log instead of 255.

// 1.78 (24.10.2021)
// Fixed - IF x THEN REM couldn't parsed by basinc, now patched, but may present new issues, due it's just a workaround.
// Fixed - When you execute a direct command, basic was corrupted temporarily. It's fixed by removing a wild syntax cropper.

// 1.77 (14.10.2021)
// Added - UDG editor character setup option
// Added - UDG editor keyboard shortcuts
// Added - Add/Edit a note to Notes Window by right clicking on a statement in listing
//         This is a step to overlay comments over program listing in a future release
// Added - Auto Show Note option in BasinC Options window. Disabling this will prevent project window to popup, even if a BAS file does contain notes.
// Fixed - save as.. Does not modify project name. (A workaround rather than a fix. Needs a bit more time)
// Fixed - Undo/redo buttonts on Image Editor (former Screen Paintbox) wouldn't work at start.
// Changed-Some Ctrl+Alt+ keyboard shortcuts was clashing with AltGR+A..U graphics mode shortcut. So all of them changed. Sorry.
// Added - Hotkey Toggle Tools. You may open *and* close following tools with single keycombo:
//         Crtl-T Tokens, Ctrl+Alt+Z Notes, Ctrl+Alt+X Tapes, Ctrl+I Image Editor, Ctrl+U Udg Editor
// Changed-English tool names Graphics/Sprite Editor become UDG Editor, and Screen Paintbox become Image Editor for simplicity.


// 1.76 (11.10.2020)
// Added - Project Notes Window
// Fixed - tooltip variables not showing correctly (hopefully fixed)
// Added - More Basinc Test Basic Programs in the release package

//1.75 (22.05.2019)
// Fixed - Parser fix (reported by: James Davis)

//1.74
// Added - Save Display Window as BMP
// Added - basin now is on github! https://github.com/ref-xx/basinc


//1.73
// Fixed - Undocumented fixes

// 1.72
// Added: -dumptxt commandline parameter. Extracts and saves BASIC portion of a basinc compatible program (eg. BAS/SNA/TAP).
//                  Usage: basinc <filename> -dumptxt   
//                  Example: basinc oregon.tap -dumptxt   (will create oregon.tap_BASIC.txt in same folder)

// 1.71

// Added: 4x,5x,6x font sizes for hi-dpi non-zoomed screens.

// Fixed: variables with 90ish numbers like a91, b95 weren't properly tokenized.


// 1.7      20.11.2017

// Added new toolbar buttons
// Added toggle breakpoint navigation buttons (see view menu)
// Added auto backup feature. Basinc saves your work in the background every 3 minutes.
//                            it keeps 10 copies going back up to 30 minutes in /autoback folder.
//                            To turn this feature off, use: Options > Filing > Auto Backup
// Changed - Due to large changes in ini and bin files, basinc now requires basinC.bin and basinC.ini, but it still uses basin.chm as help file.

// 1.7a

//  Changed - Broken Undo/Redo behaviour. BETA - Save often to avoid data loss.

//  Fixed - Right button popup menu context operators should detect *declared* variables correctly now
//  Fixed - Green Ruler Mark at the bottom of the screen should work ok even when cursor in a string.
//  Fixed - Drag&Drop files to main window works again.
//  Fixed - Esc key no longer breaks the program if Basinc is not in focus
//  Fixed - Token table wasn't printing first keywords correctly (eg. RND/SPECTRUM).
//  Fixed - File dialogs won't stuck at search results anymore
//  Fixed - Cosmetic fixes of profiling window
//  Fixed - While using double and triple size fonts, find and replace was not showing the result in the editor

//  Added - Shift+Clicking token table inserts byte code rather than token itself
//  Added - Tape Browser now accept files via drag&drop
//  Added - When in full speed emulation, a small arrow is shown at the bottom right corner of display window
//  Added - Display window preset sizes: 300%,400%,600%
//  Added - German Translation (Uwe Geiken)
//  Added - External Utility menu item. This item sends basinc's memory snapshot to an external utility, such as an emulator.


// 1.697

//  Added - SimpleCon window warns user more if it's disabled in the options
//  Added - REM speed <x> command. x is 1-50 (an integer equivalent to Mhz). It may not perform accordingly with commands which perform screen update.


// 1.696
//  Added - single instance mode
//  Added - Command line option: give filename to load
//  Added - Profiling window New (clears profiling results and starts new profiling) and Refresh (shows immediate results) button.
//  fixed - token table was printing wrong keywords (again).
//  fixed - Force Break (Undo) will go back to earlier state than intended (thus overwriting your program).
