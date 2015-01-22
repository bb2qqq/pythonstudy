:%g/pattern/d                           # find line contains pattern in this file and delete that line

:%s/\(.*\)-\(.*\)-/\2-\1-/g             # 找到用 - 符号分隔的两段内容，并把它们的顺序交换

<C-d> & <C-u>                           # Scroll up and down of half screen

<C-e> & <C-y>                           # Scorll up and down of one line, can be precede by num of lines, like 10<C-e>
