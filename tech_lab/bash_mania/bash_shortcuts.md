# Wikipedia table

Search `ctrl` in this webpage: `https://en.wikipedia.org/wiki/Bash_(Unix_shell)`

Tab ↹ : Autocompletes from the cursor position.
Ctrl+a : Moves the cursor to the line start (equivalent to the key Home).
Ctrl+b : Moves the cursor back one character (equivalent to the key ←).
Ctrl+c : Sends the signal SIGINT to the current task, which aborts and closes it.
Ctrl+d
Sends an EOF marker, which (unless disabled by an option) closes the current shell (equivalent to the command exit). (Only if there is no text on the current line)
If there is text on the current line, deletes the current character (then equivalent to the key Delete).
Ctrl+e : (end) moves the cursor to the line end (equivalent to the key End).
Ctrl+f : Moves the cursor forward one character (equivalent to the key →).
Ctrl+g : Abort the research and restore the original line.
Ctrl+h : Deletes the previous character (same as backspace).
Ctrl+i : Equivalent to the tab key.
Ctrl+j : Equivalent to the enter key.
Ctrl+k : Clears the line content after the cursor and copies it into the clipboard.
Ctrl+l : Clears the screen content (equivalent to the command clear).
Ctrl+n : (next) recalls the next command (equivalent to the key ↓).
Ctrl+o : Executes the found command from history, and fetch the next line relative to the current line from the history for editing.
Ctrl+p : (previous) recalls the prior command (equivalent to the key ↑).
Ctrl+r : (reverse search) recalls the last command including the specified character(s). A second Ctrl+r recalls the next anterior command that corresponds to the search
Ctrl+s : Go back to the next more recent command of the research (beware to not execute it from a terminal because this command also launches its XOFF). If you changed that XOFF setting, use Ctrl+q to return.
Ctrl+t : Transpose the previous two characters.
Ctrl+u : Clears the line content before the cursor and copies it into the clipboard.
Ctrl+v : If the next input is also a control sequence, type it literally (e. g. * Ctrl+v Ctrl+h types "^H", a literal backspace.)
Ctrl+w : Clears the word before the cursor and copies it into the clipboard.
Ctrl+x Ctrl+e : Edits the current line in the $EDITOR program, or vi if undefined.
Ctrl+x Ctrl+r : Read in the contents of the inputrc file, and incorporate any bindings or variable assignments found there.
Ctrl+x Ctrl+u : Incremental undo, separately remembered for each line.
Ctrl+x Ctrl+v : Display version information about the current instance of Bash.
Ctrl+x Ctrl+x : Alternates the cursor with its old position. (C-x, because x has a crossing shape).
Ctrl+y : (yank) adds the clipboard content from the cursor position.
Ctrl+z : Sends the signal SIGTSTP to the current task, which suspends it. To execute it in background one can enter bg. To bring it back from background or suspension fg ['process name or job id'] (foreground) can be issued.
Ctrl+`_` : Incremental undo, separately remembered for each line.
Alt+b : (backward) moves the cursor backward one word.
Alt+c : Capitalizes the character under the cursor and moves to the end of the word.
Alt+d : Cuts the word after the cursor.
Alt+f : (forward) moves the cursor forward one word.
Alt+l : Lowers the case of every character from the cursor's position to the end of the current word.
Alt+r : Cancels the changes and puts back the line as it was in the history.
Alt+u : Capitalizes every character from the cursor's position to the end of the current word.
Alt+. : Insert the last argument to the previous command (the last word of the previous history entry).


Ctrl + A    Go to the beginning of the line you are currently typing on
Ctrl + E    Go to the end of the line you are currently typing on
Ctrl + L    Clears the Screen, similar to the clear command
Ctrl + U    Clears the line before the cursor position. If you are at the end of the line, clears the entire line.
Ctrl + H    Same as backspace
Ctrl + R    Let’s you search through previously used commands
Ctrl + C    Kill whatever you are running
Ctrl + D    Exit the current shell
Ctrl + Z    Puts whatever you are running into a suspended background process. fg restores it.
Ctrl + W    Delete the word before the cursor
Ctrl + K    Clear the line after the cursor
Ctrl + T    Swap the last two characters before the cursor
Esc + T  Swap the last two words before the cursor
Alt + F  Move cursor forward one word on the current line
Alt + B  Move cursor backward one word on the current line
Tab      Auto-complete files and folder names


Moving the cursor:

  Ctrl + xx  Toggle between the start of line and current cursor position
Editing:

 Ctrl + L   Clear the Screen, similar to the clear command

  Alt + Del Delete the Word before the cursor.
  Alt + d   Delete the Word after the cursor.
 Ctrl + d   Delete character under the cursor
 Ctrl + h   Delete character before the cursor (Backspace)


  Alt + t   Swap current word with previous
 Ctrl + t   Swap the last two characters before the cursor (typo).
 Esc  + t   Swap the last two words before the cursor.

 ctrl + y   Paste the last thing to be cut (yank)
  Alt + u   UPPER capitalize every character from the cursor to the end of the current word.
  Alt + l   Lower the case of every character from the cursor to the end of the current word.
  Alt + c   Capitalize the character under the cursor and move to the end of the word.
  Alt + r   Cancel the changes and put back the line as it was in the history (revert).
 ctrl + _   Undo

 TAB        Tab completion for file/directory names
For example, to move to a directory 'sample1'; Type cd sam ; then press TAB and ENTER. 
type just enough characters to uniquely identify the directory you wish to open.

History:

  Ctrl + r   Recall the last command including the specified character(s)
             searches the command history as you type.
             Equivalent to : vim ~/.bash_history.

  Ctrl + s   Go back to the next most recent command.
             (beware to not execute it from a terminal because this will also launch its XOFF).
  Ctrl + o   Execute the command found via Ctrl+r or Ctrl+s
  Ctrl + g   Escape from history searching mode
        !!   Repeat last command
      !abc   Run last command starting with abc
    !abc:p   Print last command starting with abc
        !$   Last argument of previous command
   ALT + .   Last argument of previous command
        !*   All arguments of previous command
^abc­^­def   Run previous command, replacing abc with def
Process control:

 Ctrl + C   Interrupt/Kill whatever you are running (SIGINT)
 Ctrl + l   Clear the screen
 Ctrl + s   Stop output to the screen (for long running verbose commands)
            Then use PgUp/PgDn for navigation
 Ctrl + q   Allow output to the screen (if previously stopped using command above)
 Ctrl + D   Send an EOF marker, unless disabled by an option, this will close the current shell (EXIT)
 Ctrl + Z   Send the signal SIGTSTP to the current task, which suspends it.
            To return to it later enter fg 'process name' (foreground).
