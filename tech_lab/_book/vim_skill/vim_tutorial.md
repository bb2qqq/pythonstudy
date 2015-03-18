** (n) in this tutorial means you should type a number, `()` should not be present in your command **
** (a-z) means type a character between a to z, `()` should not be present in your command **

### Basic Navigation

** general text navigation **

    w       Go to the beginning of next word
    W       Go to the beginning of next WORD
    e       Go to the end of current word
    E       Go to the end of current WORD
    b       Go to the beginning of previous word
    B       Go to the beginning of previous word

    (n)<space>      Go to the nth character starts from current position
    (n)l    Has same effect as (n)<space>, l is short for letter
    (n)|    Go to the nth letter of current-line
    :goto (n)        Go to the nth character from the start of file

    7<space>        Go to the 7th character count from current position
    7l      Has same effect as 7<space>
    20|     Go to the 20th letter of current-line.
    :goto 15        Go to the 15th character from the start of file

    g_      Go to the last non blank character of current line
    H       Go to the first line of current screen.                 # H for Head
    M       Go to the middle line of curret screen.                 # M for Middle
    L       Go to the last line of current screen.                  # L for Last-line

> A `WORD` is any continue non-blank characters separate by white spaces,  
> mean while a `word` is any continue alphanumeric chars(and `_`) separate by white spaces.  

** plain text navigation **

    {       Go to the beginning of current paragragh
    }       Go to the beginning of next paragragh
    [[      Go to the beginning of current section
    ]]      Go to the beginning of next section
    (       Go to the beginning of previous sentence
    )       Go to the beginning of next sentence

> A sentence ends at a `.`, `!`, or `?` followed by new-line, tab or space.  
> Append any number and any combanation between `'`, `"`, `]`, `)` to `.`, `!`, or `?` will not break a sentence.  
> A paragragh begins after each empty line, and also at pairs of characters specified in the `paragraphs` option.  
> A section begins after a (`<C-L>`) in the first column and at each pairs of characters in the `sections` option.  
> ** In my vim config, section move in python file will jump between classes. **

** screen navigation **

    zz      Put current-line on the middle of screen
    zt      Put current-line on the top of screen
    zb      Put current-line on the bottom of screen

    :0      Go to the top line of file    - method 1
    :$      Go to the bottom line of file - method 1
    :(n)    Go to the nth line of file    - method 2
    1G      Go to the top line of file    - method 2
    G       Go to the bottom line of file - method 2
    (n)G    Go to the nth line of file    - method 2

    (n)%      Go to n-th percentage of file
    50%     Go to the middle of file (50th percentage)
    75%     Go to 3/4th part of file (75th percentage)

** code navigation **

    %       Go  to matching (), {}, or []
    [(      Go to previous unmatched (
    [)      Go to previous unmatched )
    [{      Go to previous unmatched {
    [}      Go to previous unmatched }

> in my vim config, % can match if block in python file, too

** insert mode navigation **

    <Arrow>           press correspond arrow keys to go to four directions
    SHIFT-<Left-Arr>  Go to the head of last word.
    SHIFT-<Right-Arr> Go to the head of next word.
    SHIFT-<Up-Arr>    Go to previous page.
    SHIFT-<Down-Arr>  Go to next page.

### Advancing Navigation

** jump **

Using `:jumps` or `:ju`(abrreviation) to view the jump location list.

    CTRL-O      Jump to previous location                   # O for outside
    CTRL-I      Jump to next location                       # I for inside
    5CTRL-O     Jump to location#5 above location#0
    5CTRL-I     Jump to location#5 below location#0

** Long-line navigation **

When you have a long-line, which shows like multiplelines on screen and is actually a single line.  
You can do these to navigate:

    gj      Scroll down a visual line
    gk      Scroll up a visual line
    g^      Go to the start of a visual line
    g$      Go to the end of a visual line
    gm      Go to the middle of current visual line

** vim command line Navigation **

You can navigate to particular position by passing arguments to vim when opening the file.

    vim +143 <filename>             Go to the 143rd line of file.
    vim +/search-term <filename>    Go to the first match searching from top
    vim +?search-term <filename>    Go to the first match searching from bottom
    vim -t TAG                      Go to the specific tag

** mark navigation **

\`  means to went to the exact position, meanwhile `'` means went to the line contains the position.

    m(a-z)      mark a position
    `a          Go to exact position of mark a
    'a          Go to the beginning of the line which contains mark a

When using `Upper case character`, you are setting global mark.  
You can using global mark to jump between files edited by the same vim session(using split).  

Using `:marks` to view all exists marks  
You will saw your self-defined marks along with some system marks.  
Here are some system marks that you can reach to.  

    `"      Go to the latest edited position of your last exit.
    `[      Go to the first character of previously changed or yanked text
    `]      Go to the last character of previously changed or yanked text
    `<      Go to the first character of the previously selected visual area
    `>      Go to the last character of the previously selected visual area
    `.      Go to the position where the last change was made
    `^      Go to the cursor position where you quit insert mode last time


> Be aware, 'a will let cursor go to the first none-blank character of the line which contains a,  
> it will not go to the first position of that line, if it preceding with spaces.  
> You can use `marks a` to view the detailed info about mark a, etc.


### Text Manipulation

** insert text **

    i             Insert text at current position
    I             Insert text at the beginning of the line
    o             Insert a newline after current line and insert text
    O             Insert a newline before current line and insert text

    s             Remove character under cursor and starts insert mode
    S             Remove current line and starts insert mode
    (n)s          Remove n characters from current position and starts insert mode
    (n)S          Remove n lines after current line and starts insert mode
    (n)c{motion}  Remove n line in the direction of motion and starts insert mode
    (n)C          Remove text from cursor to end of line and remove n more line, then go insert mode

    J             Join two lines

    p             Paste immediately after the cursor
    P             Paste immediately before the cursor

> J will add one more space for alphanum(and `_`) ending of first line.  
> two more spaces with other ending, no more space for space ending.  
> to set extra join spaces to 1 for all kinds of endings(except space ending), use `:set nojoinspaces`

** registers **

Using `:reg` to view your current register infomations  
And using `:h registers` to view detailed instructions about registers.  

Recent deleted content will appear in 0 - 9 register.  
You can paste content in register 7 using `"7p`, here `"` is the indicator symbol of register  
You can use `"fyy` to yank current like into `f register` and later use `"fp` to paste it out.  

There are nine types of registers:
1. The unnamed register `""`  
2. 10 numbered registers `"0 to "9`  
3. The small delete register `"-`  
4. 26 named registers `"a to "z or "A to "Z` (register "a and "A are equivalent)  
5. four read-only registers `":, "., "% and "#`  
6. the expression register `"=`  
7. The selection and drop registers `"*, "+ and "~`  
8. The black hole register `"_`  
9. Last search pattern register `"/`  

1. Unnamed register `""`

The latest deleted  content by "d", "c", "s", "x" or copied content by the "y" command went here.  
If named register was used (e.g.  `"xdd`), content went both to named register and `""` register.  
but `"_dd` doesn't store the deleted text in any register, I guess that's why it's called the blackhole register


2. Numbered registers `"0` to `"9`

Vim fills these registers with text from yank and delete commands.  

`"0` contains the most recent yanked content,  
unless yanked by specified a name register.  

`"1` contains the most recent deleted content,  
If the content is less than 1 line and not delete by named register, it went to `"-` instead of `"1`,  
else if the content less than 1 line is deleted by a named register, it went to that namedregister and `"1`.

With each successive delete command, Vim shifts the previous contents of `"1` to `"2`,  
and so forth, and losing the previous content of `"9`


3. Small delete register `"-`

This register contains text from commands that delete less than one line,  
except when the command specifies a named register.  
{not in Vi}


4. Named registers `"a` to `"z` or `"A` to `"Z`

Vim fills these registers only when you say so.  
Using lower case register to replace their previous contents,  
or as uppercase register to append to their previous contents.  
e.g. `"a` and `"A` refers to a same register, call it `register alpha`.  
But `"ayy` will replace the content of `register alpha` with current line, like `>` in shell,  
meanwhile `"Ayy` will append current line to `register alpha`, like `>>` do in shell.

When the '>' flag is present in 'cpoptions',  
then a line break is inserted before the appended text.

5. Read-only registers `":`, `".`, `"%` and `"#`

These are '%', '#', ':' and '.'.  You can use them only with the "p", "P",  
and ":put" commands and with CTRL-R.  {not in Vi}

    ".      Contains the last inserted text

    ":      Contains the most recent executed command-line.
            Example: Use "@:" to repeat the previous command-line command.

    "%      Contains the name of the current file.

    "#      Contains the name of the alternate file.    # don't know how to use this


6. Expression register `"=`

  # Didn't understand how to use it for now.

7. Selection and drop registers `"*`, `"+` and `"~`

Use these registers for storing and retrieving the selected text for the GUI.

Note that there is only a distinction between `"*` and "+ for X11 systems.  
For an explanation of the difference, see x11-selection.  

**Briefly speaking, `"*` works for vim visual selection, `"+` works for clipboard.**

The read-only "~ register stores the dropped text from the last drag'n'drop operation.  
\# A basically useless register for me.


8. Black hole register `"_`

When writing to this register, nothing happens.  This can be used to delete  
text without affecting the normal registers.  When reading from this register,  
nothing is returned.  {not in Vi}

9. Last search pattern register "/
Contains the most recent search-pattern.  This is used for `n` and `hlsearch`.  
It is writable with :let,   
you can change it to have 'hlsearch' highlight other matches without actually searching.  
You can't yank or delete into this register.  
The search direction is available in v:searchforward.  

You can write to a register with a `:let` command. Example:

        :let @/ = "the"


** insert content to clipboard **
With the knowledge of these registers, let's learn how to insert file from vim to file.  

    :%y+        Copy the whole file to clipboard
    :y+         Copy the current line to the clipboard
    :N,My+      Copy line N to line M to the clipboard
