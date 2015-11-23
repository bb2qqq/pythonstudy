
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
> Append any number and any combination between `'`, `"`, `]`, `)` to `.`, `!`, or `?` will not break a sentence.  
> A paragraph begins after each empty line, and also at pairs of characters specified in the `paragraphs` option.  
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

Using `:jumps` or `:ju`(abbreviation) to view the jump location list.

    CTRL-O      Jump to previous location                   # O for outside
    CTRL-I      Jump to next location                       # I for inside
    5CTRL-O     Jump to location#5 above location#0
    5CTRL-I     Jump to location#5 below location#0

** Long-line navigation **

When you have a long-line, which shows like multiple lines on screen and is actually a single line.  
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

Using `:reg` to view your current register informations  
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
    "# Stores the value of an expression
    "# Example:

    "# Command mode command
    :let L = [1,2,3]

    "# Normal mode command
    "# <C-M> refers to Control + M, or <Return> or <Enter> key.

    "=L<C-M>p
    1
    2
    3

7. Selection and drop registers `"*`, `"+` and `"~`

Use these registers for storing and retrieving the selected text for the GUI.

Note that there is only a distinction between `"*` and "+ for X11 systems.  
For an explanation of the difference, see x11-selection.  

**Briefly speaking, `"*` works for vim visual selection, `"+` works for clipboard.**

The read-only "~ register stores the dropped text from the last drag'n'drop operation.  
\#  basically "~ is a useless register for me.


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

    :%y+        Copy the whole file to clipboard

### Write Content

To write whole content of current file to another file, you use:

    :w newfilename

Or you can specify the line range

    :3,7w newfilename


### Power if dot

The dot `.` can repeat the last file-content-affecting command


### Power of :g

`:g` is short for global, it execute cmd on a per line basis

    :[range]g[lobal]/{pattern}/[cmd]

Excute [cmd] (default ":p") on the lines in the [range] which does match {pattern}

    :[range]g[lobal]!/{pattern}/[cmd]

Same as above but do [cmd] on those line which doesn't match the pattern.

> `:v` act the same as `:g!`

Examples:
    :g/evil/d       # Delete lines with 'evil' in it,  line with 'devil' and 'Sheviland' is count in
    :g/^$/d         # Delete all empty lines
    :g/^\s*$/d      # Delete all empty and all blank lines
    :g//m0          # Reverse a file

### Abbreviation
**Abbreviation both works in command line and insert mode**

Like `ab pa set paste` will expand `pa` into `set paste` both in your command mode and insert mode.  
Thus you'll never be able to type a single pa in insert mode.  
Unless you type `pas` and then delete `s` or paste a `pa` in like I do.  
So, it may cause some unitended trouble when using this feature. Be cautious.  

To solve problem above, you can use `iabbrev` or `ia` for insert mode only abbreviation,  
and `cabbrev` or `ca` for Command-line mode only abbreviation.

To stop abbreviation for some word in your vim session, using `una that_word` in command mode.

### Macros
Vim supports macros
1. press `q` to enter recording mode.
2. press a lower case character such as `a` as the macro name
3. do your operations
4. press `q` again to quit recording
5. press `@` + `your macro name` such as `@a` to apply actions in `macro a`
6. And you can repeat a macro multiple times by press `[number]@[macro_name]`  
  such as `6@a` to repeat `macro a` for 5 times.

You can use this feature to achieve tasks that can't be easily done by Regex.

If you have mis-input something into a macro, you can edit it like this:  
1. Paste your macro from register using something like `"ap`  
2. edit the line you pasted.  
3. using `"ayy` to copy the modified content into register again.  




> `@@` will execute the previous macro

### AUTOCMD

autocmd will execute a command when the event happened if a file matches the pattern.

    autocmd {event} {pattern} {cmd}

### Programming

press `K` you can view the man-page for a keyword, such as `random` in python  
To view the nth page of a shell command, use `[number]K`

using `gd` to go to local declaration of a variable, and `gD` to the global declaration of a variable

### Writing

you can use `set spell` to check your spelling.  
`]S` will go to the next spell error,  
`[S` moves to the previous spell error,  
`z=` will give a list of words as a suggestion for the error  
`zg` can identify the word under cursor as a `good word`
`zw` will mark a word as `wrong word`

>`[``]` + `s` will go next error word or rare word.


### Tab and space

`:set expandtab` will convert tab into corresponding spaces  
`:set softtab=4` will transfer tab into 4 spaces  
`retab` will convert all exists tabs in a file into spaces according to your tab-space setting.  
`set ai` will enable autoindent


### Command Line

`vim -b binaryfile` can be used to edit binary files.  
`vim -R file` or `view file` will open file in read-only mode  
And `vim -r` will list all swap file in current directory.  
By using ` vim -c '<command 1>' -c '< command 2>' file`,  
you can execute single or multiple vim commands to files once you open it.  
You can use `vim -w record_file target_file` to store those commands when you editing target\_file into record\_file.  
And later you can use `vim -s record_file another_file` to execute record_file as a vim script,  
using all the command stores in it by time order on another\_file.  


### Tabs

By using `vim -p file1 file2 file3`, you'll open multiple files in different sequential tabs,  
Then you can use command belong to deal with them:  

    :tabedit(tabe) file     # open another file in current vim sessionjjjj
    :tabs                   # list all tabs
    :tabn N                 # go to Nth tab
    :tabclose(tabc)         # close current tab
    :tabdo CMD              # Execute a command in all tabs
    :tabn                   # Go to next tab
    :tabp                   # Go to previous tab


### Sessions

Vim can save your `Buffers`, `Custom Options`, `Windows size`, `current directory` in a session.  

Use `:mksession` to save current file in default `Session.vim` file.  
In each directory there is only 1 `Session.vim` file.  
And later you can use `vim -S` to read the session in default `Session.vim` file.  

You can also use `:mksession my_session_file` to specify a session file.  
And use `vim -S my_session_file` to load it.


### Vimdiff
Using `vim diff -o file1 file2` to do horizontal file visual comparison.  
When you are inside a vim session, you can use `:diffsplit file2` or `:vert diffsplit file2` to open file2 for comparison.  
`[c` and `]c` was used to go to next and previous change.  


### Directory Navigation

You can use `vim directory_name` to navigate a directory.  
You use `<ENTER>` to open a file or gointo a directory in current window,  
and `o` to open a new window to show it.  
Press `D` to delete file under the cursor,  
Press `R` to rename the file,  

When you are in a vim session, you can use `Ex` to open a vim file explorer for current directory.  
Or `Ex /specific/directory` to open a new file explorer split for specific directory.  
`Sex` and `Vex` are used to open `Horizonal` or `Vertical` split for file explorer.  
Meanwhile `Tex` will open a new tab for current file explorar.  


### Multiple files

To open another file in current vim session, use `:e another_file`  
`:ls` is used to list all current editing files  
`:e #N` can go to the Nth file listed by `:ls`.  
`:next` is used to go to next file.  
`:previous` is used to go to previous file.  


### Pattern search
`[I` will show all lines contain the word under the cursor,  
and `]I` will show lines cotains matched keyword after current position.  

`??` or `//` can repeat previouse reverse or forward pattern searching.  
`*` and `#` will go next/previous match for the word under the cursor,  
while `g*` and `g#` will search for partial matching for current word.  


### Line motion

`fX` will go to character X within a line in forward direction,  
while `FX` will do it in reverse direction.  
`tX` and `TX` does the samething, but they go to previous position of searched character.  
`;` will repeat last `f/F/t/T` command in forward direction,  
`,` does it in backward direction.  


### Command mode motion

`CTRL-B` will back to the beginning.  
`CTRL-E` will go to the end.  
`CTRL-U` will delete all content before the cursor.  
`CTRL-R` + `Register_name` can paste the content of specified register into command-line.  
`CTRL-W` will delete the word before the cursor.  
`SHIFT-left/right` can move around by words.  
`Up/Down` will search the previous and next command.  
`CTRL-P` and `CTRL-N` will do the same job as `Up/Down`  
`CTRL-D` will do the command mode auto-completion.  
`CTRL-C` will quit the command mode.  

### Auto-completion

Pressing `CTRL + N` to do forward completion and `CTRL + P` to do backward completion for a word mentioned in the file.  
When in inserting mode, press `CTRL-X CTRL-L`, you can auto-complete a line with the beginning words.  
`CTRL-X CTRL-F` works for file name auto-completion in current directory.  
`CTRL-X CTRL-K` will help you to spell a word with your dictionary file.  
`CTRL-X CTRL-T` will invoke a Thesaurus word searching if you set a thesaurus dict in your vimrc.  


### Folding

In vim, you can fold lines to simplify navigation.  
`:range fold` can fold lines in the specific range.  
`zf<Navigation>/<Visual Selection>zf` will fold the lines of Navigation moves by.  
`zd` will delete(unfold) a fold under the current cursor,  
`za` will toggle the fold below the cursor.  
`zR` will unfold all folds,  
`zM` will fold everything back.  

### Vimgrep

You can use `:vimgrep pattern * ` to search pattern in all files of current directory,  
and jump to the first file which contains match pattern.  
`:cn` and `:cN` are used to jump to next and previous match patterns.  
`:clist` will list all lines in all files which match the pattern.  
To do recursive search, you can use `:vimgrep pattern **/*file_type `  


### Tricks

Press `ga` to view the decimal, hex and octal value of the character in ASCII.


Ex mode was using for continuous command execution.  
Type `gQ` or `Q` to enter it, `vi` or `visual` to exit it.  
Compare to `Q`, `gQ` support command-line motion and completion.  

You can use `:digraphs` to view special codes, then in insert mode, type `CTRL-K` plus `its digraph-code` to type it.

`:changes` can show all changes in current file.

`gqap` seems can format a paragraph in a mysterious way, you can try use `:h gqap` for some details.

To add a `#` before selected lines, first you use `CTRL-V` to select the beginning of these lines,  
Then press `I`, add `#` in the first line

`:set incsearch` will search the pattern once you type your first letter.

`s/pattern/new\_word/g [number]` will only substitute pattern in the next `[number]` lines beginning from current line.

`:X` can save and encrypt current file, interesting, though breakable.

To do full word substituion, use `:s^\<word\>^new_word^g`  
when doing a global confirmation substituion use `:%s/pattern/word/gc`,  
`a` will confirm all substitution, while `l` will subsitute current word as the last substituion then terminate the confirmation.  

To open a file in same window, type `gf` when your cursor is on that filename.  
To open a file in a new window, type `CTRL-W f`  
To open a file in a new tab, type `CTRL-W gf`  

`@:` can repeat last command line

using `:[number] split` or `:[number] vsplit` to open a split with `[number]` columns

Like `w`, `up`(update) can also write file, but it only write when content changes,  
this can avoid meaninglessly change the file modify-time.

Put your cursor on a number, press `CTRL-A` will add 1 to it, and `CTRL-X` to decrease the number by 1

view advance line info, you can use `g CTRL-G`, which is slightly powerful than `CTRL-G`

If your vim version is greater than or equal `7.0`  
You can sort the content of a file by using `:sort`  
You can sort part of a file by using visual select plus `sort`  
`:1,8sort` also sort line from 1 to 8 as intended.  
`:sort i` will ignore the case  
`:sort!` will sort in reverse order  
meanwhile `:sort u` will remove duplicate lines.  
All these flags can be combined, such as `:sort! ui`  
What a built-in `sort` utility!

To fixing typos like "thnik", you use `xp` on the first character


### Unknown for now

`burfdo` can used to modify buffer content  
`vim --noplugin file` can edit a file without load plugins  
