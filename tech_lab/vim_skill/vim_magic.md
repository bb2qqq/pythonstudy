### Run vimdiff in colorless mode

    TERM=vt100 vimdiff file1 file2

> You can even use `TERM=vt110` to make an intended error parameter,  
> in order to cancel the highlights.


### Define a user command
You use `:command Your_command_name command_text` to diy command:
Such as:

    :command Hi echo "Go and suck my dicks!"
    :Hi

> DIY command must starts with upper class letters.

### Encrypt a file
    :X
> Be aware, after you encrypted a file, you must use `:wq` to save your encryption.  
> Using `:q` will leads to a no-warning quit, and your encryption abandoned

### Show special chars in vim
    :set list

### Redirect echoed content of command to file
    redir => zen_temp | exe "my expressions" | redir END | put=zen_temp

### Redirect values of expressions to file
    :put = @%
    vim_magic.md

### Show all User Defined Functions
    :function

> To show the code of a particular function, you use `:function FunctionName`

### Multiple commands in one line
    echo "first echo." | echon "Second echo without prepend newline." | echo "Third echo"


### Echo highlight content
    echohl Title     "Specify the highlight styleyou prefer here, here `Title` can be replaced by other styles such as `Visual`.
    echo "Intended highlight contents"
    echohl None      "# Stop echo highlight signal

### Source an external vim-script
    :so my_vim_script
    :source my_vim_script

### List all search patterns in a file
With line number:
    :g/pattern/#

Without line number:
    :g/pattern/p


### Substitute all alphabete to a particular symbol
    :substitute/\a/*/g

### Enter vim shell(Ex mode)
    Q

### Execute command expressions
    :execute "echo 'my command expressions'"

### Make your vim fake death
    # Fake death for 10 seconds
    :sleep 10

    # Fake death for 50 milliseconds
    :sleep 50m

### Open command-line window
    q:

> when you already in command line, press CTRL-F to enter command window

### Make incremental list or decremental list easily
    raw data: 0 0
    command: qa0CTRL-AwCTRL-Xyypq5@a
    result:
            1 -1
            2 -2
            3 -3
            4 -4
            5 -5
            6 -6
            6 -6

### Unfold all
    zR

### Change a file into python list data
    :%s/^/"/g | %s/$/",/g | 1s/^/[/ | $s/$/]/

### Multiple command abbreviations
    ca multi_abbr command1 <bar> command2 <bar> command3

### substitue content of last line
    $s/pattern/result/g
> .   current line    :.w single.txt  
> .+1,$   line after current line to end    :.+1,$s/old/new/g
> .,.5    same (.5 is interpreted as .+5) :.,.5s/old/new/g

### Solve buftype no write issue(make a file writable)
    set buftype=

### Others

Replace pattern with pattern + newline (using \r instead of \n)
    s/pattern/pattern\r/

None greedy version for `.*`
    .\{-}

Increment 1 to the first number in the specified line-range:
    :4,8s/\d\+/\=submatch(0) + 1/


Show current\_line info
    <ctrl> + G

Write something into register, here we use `"2`
    :let @2 = "scooter"

Repeat last executed command-line
    @:                  #  : refers to ": register here


Paste content neatly.

    set paste


Go definition of current attribute

    gd


### Navigation
    <CRTL> + f/b    # Forward or backward 1 screen
    <CRTL> + u/d    # Upward or downward 0.5 screen (Upward=Forward, downward=backward)
    <CRTL> + y/e    # Go up or down 1 line

You can preced a number before press the combo key. And the motion will multiply that number. So `3<CTRL>y` will go 3 lines up.  
You can also set `nnoremap <C-e> 2<C-e>` in your vimrc to make your `<CTRL>e` goes two lines down when you press them everytime.


### Switching Case

There are two ways of switching cases in vim.
1. Under `visual mode`, select some content, press `~` to togglebetween case, `u` to switch to lower case, `U` to swith to upper case

2. using `gu/gU/g~ + {motion}`,  works for normal mode

* change word case
      g~iw        # switch the case status of an inner word

> `iw` stands for inner word, alphanumeric chars connect by `_` or other alphanumeric chars was considered a word, `KEff213E` and `apple_123` are two inner words, using `:h iw` to view more details


* change line-range case
      gu3j        # count 3 lines down from current line, make the content of these 4 lines lower case
      gU1G        # go from the current line to the first line, make these two lines every_line between them upper case.
      gU'a        # go from the current line to the line of marka, make these two lines every_line between them upper case.

> `guu`, `gUU`, and `g~~` will lower, upper, toggle the case of current line. It seems double verb means do action to current line, like `yy`, `dd` do. I can investigate this assumption in the future.


* change position-range case

      ~           # Toggle character under the cursor
      3~          # Toggle next 3 character starts from cursor
      g~`a        # go from the current position to mark a, switch case for characters on these two positions and every character between them.
      g~$         # Toggle case from current position to the end of current line



### UNSORTED

* find line contains pattern in this file and delete that line

      :%g/pattern/d

* 在本文件里寻找所有用 - 符号分隔的两段内容，并把它们的顺序交换

      :%s/\(.*\)-\(.*\)-/\2-\1-/g

* Scroll up and down of half screen

      <C-d> & <C-u>

* Scorll up and down of one line ( can be precede by num of lines, like 10<C-e> )

      <C-e> & <C-y>

* 删除本文件内所有行尾部的空格

      :%s/\s\+$//g

* 将所有与非特殊符号字符的pattern替换掉，特殊符号可以是空格，标点，\t等。在此命令中，pattern只能为字母或数字

      :%s!\<PATTERN\>!TARGET_VALUE!gc

> \<和\>分别表示 PATTERN 前和 PATTERN 后的任意符号, 如`s!\<vi!VIM!` 会将 &vi 里的vi替换成VIM， 而不会替换 avi 里的 vi。

* Ignore capitalization when doing pattern searching

      :s!PATTERN!TARGET_VALUE!i

* Add a newline start with <br> on the top of the line which starts with `*`

      :%s/^\*.*$/<br>\r&/gc

> \r is a cross-platform symbol which means press down the enter/return key


### VIMRC

* This will apply specified vim configurations when vim find the filetype is python

      autocmd FileType python set tabstop=8|set shiftwidth=4|set softtabstop=4|set expandtab

> autocmd can allow lots of automatic operation when meets the specified event, it is powerful.
