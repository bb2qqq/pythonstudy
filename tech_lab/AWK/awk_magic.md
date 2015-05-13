# AWK简易使用手册

最棒的awk tutorial是 [这个][1]， 强力推荐阅读

<br>

如果不想阅读大段的英文，以下为本人自己整理的一些心得:

> _Bug 反馈可以直接找我本人( if you can )， 或是发送邮件到 juchen.zeng@kaiqigu.com / zengjuchen@gmail.com_

<br>
---------

### 基础知识 ###

awk 的运行原理是扫描文件(或pipe输出)的每一行，然后将你编写的awk程序逻辑应用到该行文本上。

默认情况下， awk会用任意空白做列输入分隔符把每一行分成若干列。  
$1 代表第一列，$2 代表第二列，依次类推; 而 $0 代表的是整行。

文本文档raw里包含以下内容：

    I'm                 rich!
        It's   True.

运行`awk '{print $1, $2}' raw`， 你会得到：

    I'm rich!
    It's True.

我们可以看到，awk的默认输出列与列之间是按空格间隔的， 空格在这里叫列输出分隔符。

列输入分隔符和列输出分隔符都是可以自定义的，我们在进阶技巧里可以学到。


awk的基本语法是:

    awk ' ' file/input

awk命令可以对多个file执行， 它将按顺序对每个你传入的文件都执行一遍代码逻辑。

两个单引号区域里就是你的awk 代码。

awk 代码有三个阶段，`BEGIN {}`， `{}`， `END {}`  
`BEGIN {}`在扫描文本之前运行，`{}`在扫描每行文本时运行，而`END {}`在文本扫描结束后运行  
每一个阶段的第二部分都是一个 `{}`， 这个`{}`里就包含了你要在这一阶段执行的代码，中间的阶段因为经常单独执行，所以并没有名称前缀。

让我们来一起试验以下四个命令:

    awk ' BEGIN { print "Beautiful is better than ugly." } '
    awk ' { print "AWK大法好" } '
    awk ' END { print "加钱，上船！" } '
    awk ' BEGIN { print "Hi, 文超" }  { print "你懂的" } END { print "我的支付宝账户是: wjblovehwc@ooxx.com" } ' your_file

大家会发现当执行到第二行命令时我们会进入一个交互的命令行界面，你不管输入什么，按以下回车，屏幕上就会打印出一个`AWK大法好`， 这是因为当你没有将文件或是pipe输出流传给awk时，awk会自动去读取stdin。  
而`awk ' { print "AWK大法好" } '` 的意思是，每读一行，就打印一个`AWK大法好`出来。  
还没弄懂的同学可以试一下这个命令：

    awk ' { print $1 } '

在弹出输入行的时候，随便输入一些带空格的内容如`I'm   素帕曼`. 按下回车。  
这下应该更好理解了吧？

好了，知道了基本原理后，我们就可以来学习一些搜索与打印的技巧了！

在进入技巧学习前，让我们创建一个名为my\_temp的文件, 用做awk命令的目标文件。  
但请记住，awk不仅可以作用于文件，还可以作用于其他pipe命令传过来的结果。  
比如：`ls -lhrt | awk '{print $1, "\t",  $NF}'`就可以读取`ls`的输出，打印出当前文件夹内所有文件的权限情况  
OK, 让我们把以下内容复制粘贴到my\_temp里, 然后开始我们的awk技巧学习吧！


    <TEXT1>
    In this world, almost anything has pattern.
    Some pattern are obvious.
    But somes are not.
    Only through the accumulation of experience and some kind of inspiration.
    You can touch its skin.
    These patterns are called "Scentific findings", such as the "gene"

    <TEXT2>
    alien_boy   x_man
    hot_girl    seduce_man
    stupid_boy  is_not_a_man
    horny_boy   wants_woman
    baby_boy   owns_woman


<br>
<br>
### 实用技巧 ###

* 将shell变量传给awk, 你使用`-v` flag

      SHELL_VAR='哈哈'
      awk -v my_var=$SHELL_VAR '{print my_var}' my_temp


* 搜算整行里包含pattern的行， 并打印该行

      awk ' /pattern/ ' my_temp


<br>
* 搜索指定列等于pattern的行，并打印该行，此处我用的指定列是第二列（$2)

      awk ' $2 == "pattern" ' my_temp


<br>
* 搜索指定列含有pattern(不必等于）的行，并打印该行第一列

      awk ' $2 ~ /pattern/ {print $1} ' my_temp


<br>
* 搜索指定列不等于pattern的行， 并打印该行

      awk ' $2 != "pattern" ' my_temp


<br>
* 搜索指定列不含有pattern的行， 并打印该行

      awk ' $2 !~ /pattern/ ' my_temp


<br>
* 搜索条件一 和 条件二都满足的行，并打印该行

      awk ' $1 ~ /u/ && $2 == "can" ' my_temp


<br>
* 搜索满足条件一 或 条件二的行，并打印该行

      awk ' $0 ~ /pattern1/ || $3 == "are" ' my_temp


<br>
* 使用单词are作为分隔符号，并打印每行第2列

      awk 'BEGIN {FS="are"} {print $2} ' my_temp

<br>
<br>
### 进阶技巧 ###

* 常用内置变量名一览表：

      FS (Field Separator)              输入列分隔符           # 默认值为\t
      OFS (Output Field Separator)      输出列分隔符           # 默认值为空格
      NF (Number of Field)              每行总列数

      NR (Number of Row)                行号
      RS (Row Separator)                输入行分隔符           # 默认值为\n
      ORS (Output Row Separator)        输出行分隔符           # 默认值为\n

      FILENAME                          当前文件名



<br>
* awk的匹配搜索支持正则表达式

      awk ' /^ +[abc].*an$/ ' my_temp

>  上面的pattern会搜索以a或b或c开头(a、b、c之前可以有若干空格)，以an结尾的行，并打印出来


<br>
* 你可以将基础技巧结合起来，去对每一列(column)进行正则匹配

      awk ' $1 ~ /^[abc].*boy$/ && $2 ~ /^[xyz].*man$/ ' my_temp

>  上面的命令会搜索第一列以a或b或c开始、以boy结尾，第二列以x或y或z开始、以man结尾的行，并打印该行


<br>
* 如同在python里一样，你可以用`()`把逻辑包裹起来，作为一个整体

      awk ' $1 ~ /^[abc].*boy$/ && ( $2 ~ /^[xyz].*man$/ || $2 ~ /^[opq].*woman$/ ) ' my_temp

> 上述命令会搜索第一列以a或b或c开始、以boy结尾; 第二列以x或y或z开始、以man结尾或以opq开始、以woman结束的行，并打印该行


<br>
* 如果FS(文本分隔符)只有一个字符，所见即所得;  当FS所赋值里的字符数大于等于 2 时，会启动正则表达式匹配

      awk 'BEGIN {FS="[abcde].{2}boy"} {print $2}' my_temp

> 上述命令以 a/b/c/d/e + 任意2个字符 + boy 作为分隔符，打印每行第二列(如果该行没有这个分隔符，打出来的第二列什么也没有)。  
> 如果你发现结果和你想要的不一样，你需要在一些可疑的特殊符号前面加escape符`\\`，如`\\*`表示普通的`*`字符。  
> 是的，此处单个`\`不能帮助你escape，想了解更多，请点击[这儿][2]。

<br>
* 使用逻辑模块来区分对待每一行

      awk ' { if ($1=="a") {print $1} else if ($1=="b") {print $2} else {print $NF} } ' my_temp

> 上述命令的意思是，如果该行第一列是a的话，就打印第一列，如果第一列是b的话，就打印第二列，其余情况打印第三列。  
> `NF`表示每行总的field数目，加上`$`前缀可以用来表示最后一列， 如果是 `print NF` 则会直接打印该行的field数目。


<br>
* 自定义输出格式

      awk ' BEGIN { OFS="\t"; ORS=" LOVE\n" } { print NR, NF, $0 }' my_temp

> 此awk会打印每一行的行号，列数， 和该行，行尾打印一个 " LOVE"， 每行之间用`\t`区分。  
> `NF, NR, $0` 之间的逗号表明这三个输出间有输出间隔符，如果没有逗号，三个输出列会连在一起。


<br>
<br>
### 高级技巧 ###

#####书写多行命令######

你可以把所有的awk命令写在一行里，需要的时候，你也可以把它们写成多行来提升可读性。  
最简单的拆分方法是将单行命令拆分成若干你觉得合适的显示行，在每个显示行后面加上一个`\`  
在多行的awk命令里，`\`是行连接符，出现这个符号表示本行和下一行在逻辑上是关联起来的，只不过是在显示上分离了。  
`;`是逻辑分隔符，你在某一段命令后加上`;`表示这段命令和下段命令逻辑上是没有联系的，哪怕它们在同一行内。  
换行符(new line,)会根据情况等效于`\`或`;`  

> 个人亲测在bare的for/if block如` for (uid in my_dict)` 或 `if (total > 3)`后面，换行符等同于`\`  
> 在其他情况下，换行符等同于`;`  
> 仍可能存在我的测试未能覆盖到的例外情况，如有遇到，烦请告知  
> 查看更多相关讨论，请移步此[链接][4]


> _关于换行符_  
> 换行符的通俗解释是开新的一行，如你把`print $2`变成  
> print  
> $2  
> 你就是在`print`和`$2`间加了一个换行符，换行符的显示效果就是换了一行。  
> 不同系统下的换行符是不一样的，Linux下是\n， windows下是\r\n  
> 如果仍有疑惑的话，开个python，输入`print "我要开始\n\n\n换\n\n行\n了！"


如下两段代码可以体现出`;`和`\`的区别：  

    代码1

    awk '{
    print
    $2
    }' my_temp


    代码2

    awk '{
    print   \
    $2
    }' my_temp

代码1会将file里的每一行打印出来，而代码二则会打印file里的第二列。  
这是因为代码1里换行符起了`;`的作用，所以它实际上等同于`awk '{print; $2}' file`， 它的意思是遇到每行就打印，然后检查第二列是否存在。  
而代码二显式地添加了行连接符`\`， 它等同于`awk '{print $2}' file`， 它的含义很简单: 打印第二列。

<br>
##### awk脚本 #####

你也可以将awk命令写成脚本储存起来，用`awk -f script [file/stdin]`去执行那个脚本， 并将脚本的逻辑应用到要分析的文件或文本流上， 如:

    echo ' { print "AWK大法好" } ' >> my_awk_script
    awk -f my_awk_script my_awk_script

> 注意， 在awk脚本里， 你不需要在命令最外面包裹一对`'`.  
> 第二条命令实际上是用`my_awk_script`的逻辑去分析它自己  
> 即第一个`my_awk_script`是awk脚本，第二个`my_awk_script`内容一样，但成为了被分析的文本  
> `my_awk_script`里的awk命令会为`file/stdin`的每一行打印一个`AWK大法好`  
> 此处`my_awk_script`只有一行，所以打印了一个`AWK大法好`

另一种执行脚本的方法是将一个文本文档做成可执行脚本，同时去执行它:

    echo '#!/usr/bin/awk -f' >> executable_awk_script
    echo ' { print "AWK大法好" } ' >> executable_awk_script
    chmod u+x executable_awk_script
    ./executable_awk_script executable_awk_script

> 此处的awk系统路径各机器可能不同，请用 `whereis awk` 命令去找寻awk在你机器上的路径  
> `chmod u+x executable_awk_script`会使得当前用户对该文件拥有执行权限  
> 你会看到两行`AWK大法好`，因为`executable_awk_script`的内容有两行  

在awk脚本里，如果你要添加注释的话，在行首加一个`#`符号即可

<br>
##### awk运算符 #####
你可以在awk里进行数字计算，以下是一些常规的awk运算演示：

    Expression  Result
      7+3         10
      7-3         4
      7*3         21
      7/3         2.33333
      6/3         2
      7%3         1
      7 3         73    # 空格会把后面的数字和前面的数字像字符一样拼接在一起，多个0仍是0， 如`1 00 50`等于`1050`



awk 也继承了 C语言里的`++`和`--`，分别表示自增1和自减1，你可以用这两个符号来直接给变量赋值。  
自增符号在变量前面表示先改变值，再使用变量，放在变量后表示先使用变量，再进行运算， 如:

    awk 'BEGIN {print c++, ++c}'

将打印出`0 2`

<br>
除了++和--外，以下是另一些awk的变量运算符号：

    Operator         Meaning
      +=        Add result to variable
      -=        Subtract result from variable
      *=        Multiply variable by result
      /=        Divide variable by result
      %=        Apply modulo to variable

<br>
##### awk for 循环 #####
作为编程语言，awk里必须有for循环，事实上，它有两种for循环：

      for ( start-expression ; end-conditiona ; end-of-iteration-expression ) statement
      for ( variable in array ) statement


<br>
* 第一种for循环样例

      awk '{for(x=1;$x"";++x) print $x, x}' my_temp

> 以上的命令会将文本里每一行的每一列以单独一行的形式打印出来，并打印其列序号。

> awk会对每一行单独执行这个for命令。  
> `x=1`是for循环开始时的赋值; `$x""`是用来检查这一列是否存在，如果不存在，则循环终止，进入下一行；`++x`则表示：如果循环正常进行，在每一个循环结束前，x的值+1

> 中间的`$x`后面之所以跟了""， 是因为当某一列的值为0的时候，awk会认为0等同于false， for loop会终止，0和该行0之后的内容都不会得到打印，而`$x`后面跟的`""`会把0转换成字符，从而避免这个问题， 查看更多相关讨论，请点击[这里][3]


<br>
* 第二种for循环样例


      单行版本（行很长，请横向拖拽页面）：

      awk '$0 !~ /order_money/ { my_dict[$16] += $7 } END { for (uid in my_dict) if (my_dict[uid] > 100) print uid, my_dict[uid]}' ios_pay | sort -nk2


      多行版本:

      awk '$0 !~ /order_money/ \
           { my_dict[$16] += $7 } \
           END { for (uid in my_dict)
                 if (my_dict[uid] > 100)
                 print uid, my_dict[uid]}' ios_pay | sort -nk2


> 上述命令最开始的 $0 !~ /order\_money/是用来排除提取出来的带mysql列名的行， 第16个column是玩家uid， 第7个column是玩家充值，最后的 sort -nk2是以打印出来的第二个column作为数字基准列进行排序  
> 所以整个命令的效果是读取ios\_pay文件，将充值超过100的玩家按充值金额从低到高排序打印出来  
> 这里面的my\_dict， 是一个associative array(等同于python dict)， 但你不能直接print他，只能用key去取值，或是遍历里面的key。


在awk运行过程中，你可以使用`next`和`exit`来进行flow的控制。  
`exit`很好理解: 退出当前程序，带一个非零的值可以让系统知道你是非正常退出。  
`next`则意味者跳过当前行，进入下一行的处理过程。

     单行版本（行很长，请横向拖拽页面）：

     awk '{ if (NF > 8) error_num += 1; if (error_num >= 5) exit 1; if ($0 ~ /TEST/) next; print $0, error_num }' my_temp


     多行版本：

     awk '{ if (NF > 8) error_num += 1
            if (error_num >= 5) exit 1
            if ($0 ~ /not/) next
            print $0, error_num }'


> 上面命令会检查每一行是否列数超过8， 如果列数超过8，error\_num 变量就会+ 1，如果 error\_num的值达到5，程序就会退出运行。  
> 此外，如果在每行里找到not字符的话，就会跳到下一个字符。  
> 如果程序既没有退出，也没有跳到下一行的话，就把当前行内容和error\_num的当前值打印出来


<br>
##### 内置string函数 #####
awk里除了一些常规内置变量，还有一些内置函数，以下是常用string函数一览:

      length(string)
      index(string, search_pattern)
      split(string, array, separator)
      substr(string, position, [str_length])

<br>
* length() 使用样例

      单行版本（行很长，请横向拖拽页面）：

      awk '{ if(length($0) < 18) { print "Too short!"} else if (length($0) > 25) {print "Too long!"} else {print "Just fine."} }' my_temp

      多行版本:

      awk '{
             if(length($0) < 18) { print "Too short!"}
             else if (length($0) > 25) {print "Too long!"}
             else {print "Just fine."}
           }' my_temp


> 如果整句长度小于18，打印"Too short!"， 如果整句长度大于25， 打印"Too long!"， 其余情况，打印"Just fine".


<br>
* index() 使用样例

      awk '{print index($0, "boy")}' my_temp

> 在每行里搜索单词boy开始的位置，并打印该位置，0表示该行里没有better单词


<br>
* substr() 使用样例

      awk '{print substr($1, 2)}' my_temp
      awk '{print substr($1, 2, 5)}' my_temp

>  样例1：截取每行第1列第2个字符到第1列最后一个字符， 并打印出来  
>  样例2：从第1列第2个字符开始，截取5个字符长度的string（只截取第一列的，截完为止）， 并打印出来


<br>
* split() 使用样例

      awk '{ split($1, TempArray, "_"); print TempArray[2] }' my_temp

> 使用`_`分隔符对每行第一列进行二次分隔，并将所得字符片段按序号写入字典TempArrary里， 最后打印第2段字符（字符序号从1开始计算）。


### 私の黑魔法 ###

* AWK里打印单引号
      awk '{print "\x27"}'

* 搜索消费日志里与目标服务器相符的行(截取了第二个column第1个字符到第-7个字符)

      awk -v server=$i 'substr($2, 1, length($2) -7) == server' mix_spend  > server_spend


* 显示当前文件夹下所有文件的权限

      ls -lhrt | awk '{print $1, "\t",  $NF}'

<br>
* 生成admin玩家名单

      awk '$10 ~/admin/ && $13 ~ /代充/ {print $15}' /data/sites/zengjuchen/mix_pay_all | sort -u | awk 'BEGIN{print "admin_qiku=["} {print "\""  $0  "\","} END {print "]"}' > admin_qiku.py

> `mix_pay_all`是玩家的mysql付费记录， `sort -u`用来给玩家uid去重, 这条命令直接生成 admin\_qiku.py的python文件，里面有一个列表，是所有admin玩家的uid。

<br>
* 某一列求和

      awk 'BEGIN {total=0} {$total+=$1} END {print $total}' file/pipe_stin

> 作为编程语言，awk可以声明变量，并为其赋值， 此处我们声明了一个total变量，并将每行第一列的值与其相加，在最后打印total的值。

[1]: http://www.grymoire.com/Unix/Awk.html#uh-1
[2]: http://unix.stackexchange.com/questions/183244/why-awk-understand-fs-but-not-for-fs
[3]: http://unix.stackexchange.com/questions/149234/how-to-understand-the-command-awk-forx-1xxprint-x
[4]: http://unix.stackexchange.com/questions/183628/when-will-awk-treat-newline-character-as-and-when-not/183631?noredirect=1#comment305993_183631
