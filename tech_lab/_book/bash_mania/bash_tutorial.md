shell 是用来帮助人和机器交流的中间层。它将人的命令转化为机器能听懂的语言。terminal是shell的外观，人的输入和机器的反应会显示在它的外观上。

Bourne Shell是unix上最早的shell, 它叫这个名字是因为最早作者的名字里有`Bourne`这个词，它写于1970s。由于它是最早的shell,所以缩写是`sh`。而bash则是另一个家伙在1989年写的，里面加入了一些增强特性。为了表达对`Bourne Shell`作者的敬意，这个新shell的名字叫`Bourne Again Shell`, 尽管新作者的名字和`Bourne`没有半毛钱关系。而这个新shell的缩写则是我们现在广泛使用的`bash`

开一个新terminal窗口的时候会开启一个shell进程

`echo $$`可以打印出当前shell的进程id



`$?`是上一条命令或脚本的执行状态，0是成功，1是报错。
bash最多支持256种退出状态，即0到255。可以用`awk 'BEGIN {exit 258}'; echo $?`命令来验证这一点。

在没有双引号的情况下`$*`和`$@`作用相同，而加了双引号后，`"$*"`会把所有的variable用引号包起来，`"$@"`则会把接受的variable一个个用引号包起来, 试看下例：

    vim t.sh

    for i in "$*"
        do
            echo $i
        done

    for i in "$@"
        do
            echo $i
        done

接着，你输入`sh t.sh WJB I`, 你会得到:

    WJB I
    WJB
    I

看到区别了？


Shell里有arrary,可以用来存储各类value, 但index只能是数字。

初始化一个array，我们用`Hero=(Illidian Arthas Lich-King)`

打印array里某一个序号的值, 比如2，你使用`echo ${Hero[2]}`

打印array里所有value, 你使用 `echo ${Hero[*]}` 或 `echo ${Hero[@]}`





Conditional expression should be wrapped in `[]`, like `[ $a != $b ]`

Relational Operators only works between variables have numeric value, or number like string value, such as `"32"`, here is a table, in which `$a=10` and `$b=20`:

Operator       Description                      Example
-eq              equal                          [ $a -eq $b ]     False
-ne              not equal                      [ $a -ne $b ]     True
-gt              greater than                   [ $a -gt $b ]     False
-lt              less than                      [ $a -lt $b ]     True
-ge              greater than or equal          [ $a -ge $b ]     False
-le              less than or equal             [ $a -le $b ]     True


在所有的Conditional Expression里，变量和`[`之间必须有一个空格，像`[ $a >= $b ]`.  
而`[$a >= $b]`则会导致错误发生。

