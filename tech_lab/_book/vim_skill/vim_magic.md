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


### VIMRC ###

* This will apply specified vim configurations when vim find the filetype is python

      autocmd FileType python set tabstop=8|set shiftwidth=4|set softtabstop=4|set expandtab

> autocmd can allow lots of automatic operation when meets the specified event, it is powerful.
