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

In shell there are also Boolean Operators, they can be used in condition judge.

Operator       Description          Example
!                not                [ ! false ]                  True
-o               or                 [ $a -gt 35 -o $b -eq 15 ]   False
-a               and                [ $a -ge 9 -a $b -le 20 ]    True


There are also operators works for strings, imagine `$a` holds "abc" and `$b` holds "efg", then:

Operator        Description             Exampele
=                  equal                [ $a = $b ]         False
!=              not equal               [ $a != $b ]        True
-z              str is zero byte?       [ -z $a ]           False
-n              str is none-zero byte?  [ -n $b ]           True
[str]             is empty string       [ $a ]              True


In unix we even have operators for files! Let's assume our `file` has size of 100 bytes with read, write, and execute permissions.

Operator        Description                                 Example
-b file         Is block speicial file?                     [ -b $file ]    False
-c file         Is character special file?                  [ -c $file ]    False
-d file         Is a directory?                             [ -d $file ]    False
-f file         Is an ordinary file?                        [ -f $file ]    True
-g file         Has group ID set on?                        [ -g $file ]    False
-k file         Has sticky bit set on?                      [ -k $file ]    False
-p file         Is named pipe file?                         [ -p $file ]    False
-t file         File descriptor open & bind to terminal?    [ -t $file ]    False
-u file         Has user id set on ?                        [ -u $file ]    False
-r file         Readable?                                   [ -r $file ]    True
-w file         Writable?                                   [ -w $file ]    True
-x file         Executable?                                 [ -x $file ]    True
-s file         Size greater than 0?                        [ -s $file ]    True
-e file         Exists?(works for directory, too)           [ -e $file ]    True

> if `stick bit set` is on for a file, except the file owner and root, no one else can delete other users data in this file.


Normally, we use condition judgement to do decsion making. There are two ways to do so, the first one is `if ... then ... n*([elif] ... [then] ...) [else] ... fi` structure

Belowing is an oneline if statement:

    a=10;b=20
    if [ $a -le $b ]; then echo "yes"; fi

You can add multiple `elif ... then ...` block into this structrue, with an optional `else ...` block.  And, don't forget the `fi` at the end. Belowing are 2 examples. You should run them as shell script.

    # example 1
    a=10;b=20
    if [ $a -ge $b ]
        then
            echo "A is greater than or equal to B"
    elif [ $a -lt $b ]
        then
            echo "A is less than B"
    fi

    # example 2
    a=10;b=20
    if [ $a -ge $b ]
        then
            echo "A is greater than or equal to B"
    elif [ $a == 8 ]
        then
            echo "A is 8"
    elif [ $b == 18 ]
        then
            echo "B is 18"
    else
        echo "All the previous conditions does not match"
    fi

If you wanna do something to multiple branches, you may using a nested `if ... else ...` structure, but shell has another grammer for this: `case ... esac`  
`case` structure is usually used to judge if a variable value in a particular pattern, which is hard to do in shell `if` structure. The general pattern is below:

    case $var in
        pattern1)
            command1
            ;;
        pattern2)
            command2
            command3
            ;;
        pattern3|pattern4|pattern5)
            command4
            ;;
        *)
            command5
            ;;
    esac

In the example above, the part starts from pattern2 to command5 is optional. `;;` means that the program flow would jump to the end of the case statement. so the case block will finish execution once find a match pattern.  
Let's see a usable one-line example:

    a=5
    case $a in [357]) echo "yes";; esac

And a multiple version:
    a=5;
    case $a in
        [368])
            echo "var satisfy condition 1"
            ;;
        [37] | [56])
            echo "var satisfy condition 2"
            ;;
        *)
            echo 'finish!'
    esac

> the `|` above means `or`


### LOOP

In shell, we got 4 types of loop tools: `while loop`, `for loop`, `until loop` and `select loop`, `while loop` will excute the commands as the condition is ture, `for loop` will loop over the given var range, `until loop` will execute the commands until the  belowing are 4 basic examples of these loops.

    # WHILE LOOP
    a=1
    while [ $a -lt 5 ]
        do
            echo $a
            a=$(expr $a + 1)
        done


    # FOR LOOP
    for i in {1..9}
        do
            echo $i
        done


    # UNTIL LOOP
    a=1
    until [ $a -gt 5 ]
        do
            echo $a
            a=$(expr $a + 1)
        done

    # SELECT LOOP
    select NUM in 2 3 5 7
do
    case $NUM in
        [2345])
            echo $NUM'235'
        ;;
        *)
            echo $NUM'other'
        ;;
    esac

    # SELECT LOOP 2
    select TOY in 2 3 5
    do
        if [ $TOY -gt 3 ]
            then
            echo "greater than 3"
        else
            echo "Less or equal to 3"
        fi
    done

> All these four loops listed above can be nested together to produce more variety.

You can use `continue` and `break` to do loop contral, in shell they act just like they do in python. Except you can use `continue n` and `break n` to get out of `n`th loop. Try the following two examples, you'll know what I mean.


    #!/bin/bash

    echo "break"

    for var1 in 1 2 3
    do
        for var2 in 0 5
        do
            if [ $var1 -eq 2 -a $var2 -eq 0 ]
            then
                break 1
            else
                echo "$var1 $var2"
            fi
        done
    done


    echo "continue"

    for i in 6 7 8 9 10
    do
        for j in 1 2 3 4 5
        do
            if [ $(expr $i % 2) -eq 0 -a $(expr $j % 2) -eq 0 ]
            then
                continue 2
            else
                echo "$i $j"
            fi
        done
    done


### Substitution

To assign the output of a command to a variable, simply use:

    var=`command`

And follows are different substituion of variables.

    Form                Description
    ${var}              substitute the value of var

    ${var:-word}        if var is null or unset, word is used as the substituted string, the value of var won't change
    ${var:=word}        if var is null or unset, var is set to word, then substitue begins
    ${var:+word}        if var is set, word is used as the substituted string, value of var won't change

    ${var:?message}     if var is null or unset, message will be printed to standard error.

### MetaCharacters

    * ? [ ] ' " \ $ ; & ( ) | ^ < > new-line space tab

These are special characters in shell, also named `metacharacters`. To convert  `metacharacters` to normal character, you got four way to do it

1. you can add a `\` before a single `metacharacter`.  
    echo Hello \; World!

2. you can wrap any number of any kind of `metacharacters` in single quote `'` to make them normal
    echo ' *?[]"\$;&()|^<> '

> single quote can't convert single quote, try `echo ' '' '` and `echo ' \' ' '`

3. Double quotes `"` do the similar job, except six characters or combinations below
    EXCEPTIONS FOR DOUBLE QUOTE:
        `   $   \`  \$  \'  \"  \\

4. Back quotes ` ` ` will treat what inside it as command and execute it.

    echo `date`


##### INPUT REDIRECTION

The symbol for input redirection is `<`, it reads content of file and feed them as standard input to command. Please see the example below:

    $ wc -l test
    1 test

    $ wc -l < test
    1

In the first command, `test` file was passed as a parameter to `wc`, so `wc` knows its name and prints it out.  
BUt in the second command, we directly passed the content to `wc`, so he don't know who is the owner of these content, except they comes from standinput, so no filename prints out.


`<<` is used to start a `Here` document, the pattern is like:

    command << self_defined_delimiter
        content
        ...
        content
    delimiter

It is used to feed multiple lines as text content to command. Below is an example.

    cat << 虽然我长得有点奇怪，可我真的是个delimiter，不信你试试
    第一行
            来啊
                    我是第三行
    虽然我长得有点奇怪，可我真的是个delimiter，不信你试试

Write the content above in to a file, then execute it, you'll know what `self_defined_delimiter` is. Amazing, isn't it?

There are three types of I/O, each have their own identifier, called a file descriptor:
    standard input:  0
    standard output: 1
    standard error:  2

With no file descriptor number, `<` refers to the standard input(0),  `>` and `>>` refers to standard output(1). And we can specify the part we want to redirect, just like below.

    ls non_exist_file 2> tmp

> The command above will redirect the error message of ls command to tmp file, `2>` means pass standard error to target
