#!/usr/bin/perl

# To run perl interactively, you use:
# perl -d -e 1

# Perl has the same comment way as python do, using "#"

print "Hello, world\n";      # In perl, print won't print a newline automatically
print("Parenthesis!\n");     # This parenthesis feature is the same as python3

# 在string型variable里，你可以使用\U和\L来将某个点之后的字母全变成大写或小写
print "using \\U to \U capitalize\n";
print "using \\L to \L MAKE LOWER CASE\n";

$a="老汤圆";                 # you use $x=??? to assign values to variables 
$b="小秤砣";                 # In perl, you must add a `;` after each simple statement#


# double quote can interpret vars, \n, and others, (Variables can be called directly in a string)
print "$a给$b把尿\n";        

# single quote will print out the raw infomation
print '$a给$b把尿\n';        

# 在Perl里输入多行文档，你会用到一种近似奇技淫巧的方法，请看
%multiple_line = <<"奇技淫巧";
在这里，奇技淫巧可以被替换成任何字符, 它被称作identifier
不要在 << 和identifier间增加空格
如果你使用双引号 " 来包裹你的奇迹淫巧, 那么它能将所包裹的文字里的特殊符号转义
在之前的代码里我们定义了a作为老汤圆, 我们来call一下它
召唤$a
将identifier作为单行输入表示多行文档输入结束,在identifier的前后加任意字符都会导致它失效

奇技淫巧

@raw_multiple_line = <<'奇技淫巧raw版';
如果我们用单引号包裹的话
召唤$a就会失败
奇技淫巧raw版


# 除了$, @和%也可以用来表示variable, 通常情况下@用来表示arrays(list), %用来表示hashes(dict), 但perl可以根据上下文判断变量的类型，所以此处我们用@和%表示scalar(标量)也能被perl识别,不会报错
print %multiple_line;
print @raw_multiple_line;

# perl 的list和dict都是用()包起来，区别是list变量用@开头，dict变量用%开头，而且在定义之后
@list=(1,2,3,4,5);
%dict=(1,2,3,4,5);

print "$list[0]\n";         # using [ ] to wrap index
print "$dict{1}\n";         # using { } to wrap key

print "@list[2]\n";
#print %dict{2};

# 骇人听闻的奇技淫巧又来了
@names

