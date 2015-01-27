* find line contains pattern in this file and delete that line

      :%g/pattern/d

* 在本文件里寻找所有用 - 符号分隔的两段内容，并把它们的顺序交换

      :%s/\(.*\)-\(.*\)-/\2-\1-/g

* Scroll up and down of half screen

      <C-d> & <C-u>

* Scorll up and down of one line ( can be precede by num of lines, like 10<C-e> )

      <C-e> & <C-y>

* 删除本文件内所有行尾部的空格

      :%s/ \+$//g
