# AWK是一门编程语言！

最棒的awk tutorial是 [这个](http://www.grymoire.com/Unix/Awk.html#uh-1), 强力推荐阅读

<br>

以下为本人咀嚼过的二手产品, 不嫌弃就将就看一下吧:

---------

### 基础 ###

awk 的运行原理是扫描 文件(或pipe输出)的每一行，然后将你编写的code应用到该行文本上。

默认情况下， awk会用任意空白做输入分隔符把每一行分成若干列，$1 代表第一列，$2 代表第二列，依次类推。而 $0 代表的是整行。

文本文档raw里包含以下内容：

    I'm                 rich!
        It's   True.

运行`awk '{print $1, $2}' raw`, 你会得到：

    I'm rich!
    It's True.

我们可以看到，awk的默认输出列与列之间是按空格间隔的, 空格在这里叫输出分隔符。

输入分隔符和输出分隔符都是可以自定义的，我们在进阶技巧里可以学到。


awk的基本语法是:

    awk ' ' file

两个单引号区域里就是你的awk 代码。

awk 代码有三个阶段，`BEGIN {}`, `{}`, `END {}`  
`BEGIN {}`在扫描文本之前运行，*`{}`在扫描每行文本时运行*，而`END {}`在文本扫描结束后运行  
每一个阶段的第二部分都是一个 `{}`, 这个`{}`里就包含了你要在这一阶段执行的代码，中间的阶段因为经常单独执行，所以并没有名称前缀。

让我们来一起试验以下四个命令:

    awk ' BEGIN { print "我很帅" } '
    awk ' { print "我很屌" } '
    awk ' END { print "我很有钱！" } '
    awk ' BEGIN { print "我很帅" }  { print "我很屌！" } END { print "我的支付宝账户是: wjblovehwc@ooxx.com" } ' your_file

大家会发现当执行到第二行命令时我们会进入一个交互的命令行界面，你不管输入什么，按以下回车，屏幕上就会打印出一个`我很屌`, 这是因为当你没有将文件或是pipe标准输出流传给awk时，awk会自动把标准输入当做文本进行扫描。而`awk ' { print "我很屌" } '` 的意思是，每读一行，就打印一个`我很屌`出来。还没弄懂的同学可以试一下这个命令：

    awk ' { print $1 } '

在弹出输入行的时候，随便输入一些带空格的内容如`I'm   素帕曼`. 按下回车。这下应该更好理解了吧？

好了，知道了基本原理后，我们就可以来学习一些搜索与打印的技巧了！


### 实用技巧 ###




* 搜算整行里包含pattern的行, 并打印该行

      awk ' /pattern/ '


* 搜索指定列等于pattern的行，并打印该行，此处我用的指定列是第二列（$2)

      awk ' $2 == "pattern" '


* 搜索指定列含有pattern(不必等于）的行，并打印该行第一列

      awk ' $2 ~ /pattern/ {print $1} ' file/pipe_stin


* 搜索指定列不等于pattern的行， 并打印该行

      awk ' $2 != "pattern" '


* 搜索指定列不含有pattern的行， 并打印该行

      awk ' $2 !~ /pattern/ '


* 搜索条件一 和 条件二都满足的行，并打印该行

      awk ' $1 ~ /pattern1/ && $2 == "pattern2" '


* 搜索满足条件一 或 条件二的行，并打印该行

      awk ' $1 ~ /pattern1/ || $2 == "pattern2" '


* 使用单词love作为分隔符号，并打印每行第2列

      awk 'BEGIN {FS="love"} { print $2 } '



### 进阶技巧 ###

* 常用内置变量名一览表：

      FS (Field Separator) 输入列分隔符                   # 默认\t
      OFS (Output Field Separator) 输出列分隔符           # 默认空格
      NF (Number of Field) 每行总列数

      NR (Number of Row) 行号
      RS (Row Separator) 输入行分隔符                     # 默认\n
      ORS (Output Row Separator)  输出行分隔符            # 默认\n

      FILENAME  当前文件名

* 某一列求和

      awk 'BEGIN{total=0} { $total+=$1 } END {print $total}' file/pipe_stin

> 作为编程语言，awk可以声明变量，并为其赋值, 此处我们声明了一个total变量，并将每行第一列的值与其相加，在最后打印total的值。


* awk的匹配搜索支持正则表达式

      awk ' /^[abc].*z$/ '

>  上面的pattern会搜索以a或b或c开头，以z结尾的行，并打印出来


* 你可以将基础技巧结合起来，去对每一个列(column)进行正则匹配

      awk ' $1 ~ /^[abc].*boy$/ && $2 ~ /^[xyz].*man$/ '

>  上面的命令会搜索第一列以a或b或c开始、以boy结尾，第二列以x或y或z开始、以man结尾的行，并打印该行


* 如同在python里一样，你可以用`()`把逻辑包裹起来，作为一个整体

      awk ' $1 ~ /^[abc].*boy$/ && ( $2 ~ /^[xyz].*man$/ || $2 ~ /^[opq].*woman$/) '

> 上述命令会搜索第一列以a或b或c开始、以boy结尾; 第二列以x或y或z开始、以man结尾或以opq开始、以woman结束的行，并打印该行


* 如果FS(文本分隔符)只有一个字符，所见即所得;  当FS所赋值里的字符数大于等于 2 时，会启动正则表达式匹配

      awk 'BEGIN {FS="con.{5}sy"} {print $2}'

> 上述命令以 con + 任意5个字符 + sy 作为分隔符，打印每行第二列(如果该行没有这个分隔符，打出来的第二列什么也没有)
> 如果你发现结果和你想要的不一样，你需要在一些可疑的特殊符号前面加逃脱符\\ (是的，在这个地方单个\尚不能帮助你逃脱,), 如`\\*`表示普通的`*`字符


* 使用逻辑模块来区分对待每一行

      awk ' { if ($1=="a") {print $1} else if ($1=="b") { print $2 } else {print $NF} } ' test

> 作为一门编程语言，基本的判断逻辑是必不可少的，上述命令的意思是，如果该行第一列是a的话，就打印第一列，如果第一列是b的话，就打印第二列，其余情况打印第三列, NF表示每行总的field数目，加上$前缀可以用来表示最后一列, 如果是 print NF 则会直接打印该行的field数目。


* 自定义输出格式

      awk ' BEGIN { OFS="\t"; ORS=" LOVE\n" } { print NR, NF, $0 }'

> 此awk会打印每一行的行号，列数, 和改行，行尾打印一个 " LOVE", 每行之间用\t区分
> NF, NR, $0 之间的逗号表明这三个输出间有输出间隔符，如果没有逗号，三个输出列会连在一起


### 高级技巧 ###

你可以在awk里进行数字计算，以下是一些常规的awk运算演示：

    Expression  Result
      7+3         10
      7-3         4
      7*3         21
      7/3         2.33333
      6/3         2
      7%3         1
      7 3         73           \# 空格会把后面的数字直接和前面的数字字面拼接在一起，多个0仍是0, 如`1 00 50` 等于`1050`


awk 也继承了 C语言里的++和--，表示自增1和自减1，你可以用这两个符号来直接给变量赋值，自增符号在变量前面表示先改变值，再使用变量结果，放在变量后表示先使用变量的值，再进行运算, 如

    awk 'BEGIN {print c++, ++c}'

将打印出`0 2`

除了++和--外，以下是另一些awk的变量运算符号：

    Operator         Meaning
      +=        Add result to variable
      -=        Subtract result from variable
      *=        Multiply variable by result
      /=        Divide variable by result
      %=        Apply modulo to variable


作为编程语言，awk里必须有for循环，事实上，它有两种for循环：

      for ( start-expression ; end-conditiona ; end-of-iteration-expression ) statement
      for ( variable in array ) statement


* 第一种for循环

    awk '{for(x=1;$x"";++x)print $x, x}'

> 以上的命令会将文本里每一行的每一个column单独成行打印出来,并打印其列序号
> awk会对每一行单独执行这个for命令。x=1是for循环开始时的赋值; $x""是用来检查这一列是否存在，如果不存在，则循环终止，进入下一行；++x表示：如果循环正常进行，在每一个循环结束前，x的值+1
> 中间的$x后面之所以跟了"", 是因为当某一列的值为0的时候，awk会认为0等同于false, for loop会终止，0和该行0之后的内容都不会得到打印，而`$x`后面跟的`""`会把0转换成字符，从而避免这个问题


* 第二种for循环

    awk '$0 !~ /order_money/ { my_dict[$16] += $7 } END { for (uid in my_dict) if (my_dict[uid] > 100) print uid, my_dict[uid]}' ios_pay | sort -nk2

> 上述命令最开始的 $0 !~ /order\_money/是用来排除提取出来的带mysql列名的行, 的第16个column是玩家uid, 第7个column是玩家充值，最后的 sort -nk2是以打印出来的第二个column作为数字基准列进行排序
> 所以整个命令的效果是读取ios\_pay文件，将充值超过100的玩家按充值金额从低到高排序打印出来
> 这里面的my\_dict, 是一个associative array(等同于python dict)


在awk运行过程中，你可以使用`next`和`exit`来进行flow的控制，`exit`很好理解，退出当前程序，带一个非零的值可以让系统知道你是非正常退出。`next`则意味者跳过当前行，进入下一行的处理过程。

    awk '{ if (NF > 8) error_num += 1; if (error_num >= 5) exit; if ($0 ~ /TEST/) next; print $0, error_num }'

> 上面命令会检查每一行是否列数超过8， 如果列数超过8，error\_num 变量就会+ 1，如果 error\_num的值达到5，程序就会退出运行，此外，如果在每行里找到TEST字符的话，就会跳到下一个字符，如果程序既没有退出，也没有跳到下一行的话，就把当前行内容和error\_num的当前值打印出来


<br>
awk里除了一些常规内置变量，还有一些内置函数，以下是常用string函数一览:

      length(string)
      index(string, search_pattern)
      split(string, array, separator)
      substr(string, position, [str_length])

* length() 使用样例

      awk '{ if(length($0) < 18) { print "Too short!"} else if (length($0) > 25) {print "Too long!"} else {print "Just fine."} }'

> 如果整句长度小于18，打印"Too short!", 如果整句长度大于25， 打印"Too long!", 其余情况，打印"Just fine".


* index() 使用样例

      awk '{print index($0, "better")}'

> 在每行里搜索单词better开始的位置，并打印该位置，0表示该行里没有better单词


* substr() 使用样例

      awk '{print substr($1, 5)}'

>  截取每行第1列第五个字符到第1列最后一个字符, 并打印出来

      awk '{print substr($1, 5, 10)}'

>  从第1列第五个字符开始，截取10个字符长度的string, 并打印出来


* split() 使用样例

      awk '{ split($1, TempArray, "---"); print TempArray[3] }'

> 使用`---`分隔符对每行第一列进行二次分隔，并将所得字符片段按序号写入字典TempArrary里，最后打印第三段字符, 序号从1开始

