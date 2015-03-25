#!/usr/bin/perl

# To run perl interactively, you use:
# perl -d -e 1

# Perl has the same comment way as python do, using "#"

print "Hello, world\n";      # In perl, print won't print a newline automatically
print("Parenthesis!\n");     # This parenthesis feature is the same as python3

# 在string型variable里，你可以使用\U和\L来将某个点之后的字母全变成大写或小写
print "using \\U to \U capitalize\n";
print "using \\L to \L MAKE LOWER CASE\n";

# In perl '' and "" works similar to their usage in shell.
# Where '' will convert all string to noraml strings,
# Meanwhile "" allows special chararcters.
# Try this statement, compare to previous example:
print 'using \\U to \U capitalize\n';


$a="老汤圆";                 # you use $x=??? to assign values to variables
$b="小秤砣";                 # In perl, you must add a `;` after each simple statement#


# Double quote can interpret vars, \n, and others, (Variables can be called directly in a string)
print "$a给$b把尿\n";

# In previous example, "给" is something separate $a and $b,
# You can also use space and . to separate,
# If you don't, you'll get an error, like below:
print "$aand$b"


# single quote will print out the raw infomation
print '$a给$b把尿\n';

# 在Perl里输入多行文档，你会用到一种近似奇技淫巧的方法，请看
# UPDATE, this is called HERE document, also valid in unix
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

# Another way to assing key-value pairs in dict
%dict = ('me' => 'dsb', 'you' => 'wise_man')

# You can also use hyphens to replace '' or "" for dict key,
# Hyphen key only support `=>` indicator, for example:
%dict = (-a => 'yoxi', -b => 'nana')

# To get keys and values from dict, you use
@index = keys %dict
@strings = values %dict

# To check the existence of a key in a dict
@a=exists($dict{-a})

# To know the size of a list, you do this:
$scalar = @list
print $scalar       # Scalar is the length of list

# Adding and remove item to dict
$dict{'new_key'} = 'wonderful'
print $dict{'new_key'}
print $dict{-a}
delete $dict{-a}
print $dict{-a}

#The ? : Operator
# operator ? : can be used to replace if...else statements.
# It has the following general form:
# Exp1 ? Exp2 : Exp3;
# Where Exp1, Exp2, and Exp3 are expressions.
# Notice the use and placement of the colon.

# The value of a ? expression is determined like this:# Exp1 is evaluated. If it is true,
# then Exp2 is evaluated and becomes the value of the entire ? expression.
# If Exp1 is false, then Exp3 is evaluated and its value becomes the value of the expression.
# Below is a simple example making use of this operator:

$a=(2>1)? 3: 4;
$b=(3>4)? 3: 4;
print $a;
print $b;

# Let's learn some formal if-else:
if (1){
    print 2;
}
if (1==1){print 2;}

# Let's try else block:
if (0) {print 0} else {print 1}

# elsif block added:
if (0) {} elsif (1>2) {} elsif (2>1) {print '2>1'} else {}

# unless will catch False expression and run the command:
unless ('baba'!='mama') {print 'fuck you'}

# Previous command doens't work as you expected
# Because, in Perl, you use `lt`, `gt`, `eq`, `ne` and `cmp` to compare strings.
# When you compare string, you don't compare thier length, instead, you compare their aplphabetic order.
# obj1 cmp obj2 will return 0 if two obj equal, return 1 if first trumps second, else, return -1.
unless ('baba' eq 'mama') {print 'fuck you'}

# Let's try a full structure, which elsif block will be excuted when unless failed,
# and elsif expression is true
unless (1==1) {print '1'} elsif (0) {print '2'} else {print '3'}

# There is a new structure named switch in new edition of perl,
# which allows action like case..esac in shell.
# You need to install Switch module first, and then add `use Switch` in your perl script.
# Basic grammer looks like followed:

switch($var){
   case 10           { print "number 100\n" }
   case "a"          { print "string a" }
   case [1..10,42]   { print "number in list" }
   case (\@array)    { print "number in list" }
   case (\%hash)     { print "entry in hash" }
   else              { print "previous case not true" }
}

# while loop in perl is similar to javascript
$height=0;
while ($height<=180)
{ print $height; height += 1}

# until loop stops when reach condition
$age=0;
until ($age==90)
{ print $age; $age+=1}

# Yet perl has a special `do... while` structure, which excute the body first,
# Then judge the while condition, if true, continue; else, abort.
$combat='突破天际';
do {
    print $combat;
   }
while ($combat >5);

# The syntax of a for loop in Perl programming language is :
# for ( init; condition; increment ){
#    statement(s);
# }
# Here is the flow of control in a for loop:
#
# 1. The init step is executed first, and only once,
# This step allows you to declare and initialize any loop control variables.
# You are not quite required to put a statement here, but semicolon is needed.
#
# 2. Next, the condition is evaluated.
# If it is true, the body of the loop is executed.
# If it is false, the body of the loop does not execute,
# and flow of control jumps to the next statement after the for loop.
#
# 3. After the body of the for loop executes,
# the flow of control jumps back up to the increment statement.
# This statement allows you to update any loop control variable,
# and can be blank with semicolon.
#
# 4. The condition is now evaluated again,
# if it is true, the loop executes and the process repeats itself
# (body of loop, then increment step, and then again condition).
# After the condition becomes false, the for loop terminates.

for ($salary=5000; $salary<50000; $salary*=2){ print "$salary\n" }

# The equivalent version of python for loop in perl is called foreach.
# But you can only use it to iter over list, not dict.
@emotion_list=('confusion', 'happiness', 'grieve')
foreach $emotion (@emotion_list) {print "$emotion\n"}

# Perl allows all kinds of nested loop, just nest it as you need!


# Some perl variables are system default and has particular meaning, visit website below for details:
# http://www.tutorialspoint.com/perl/perl_special_variables.htm


# And below is a list of perl internal functions:
# http://www.tutorialspoint.com/perl/perl_function_references.htm

# REGEX
#
# Here comes the most exciting part, regex in perl:
# The basic method for applying a regular expression is to use the pattern binding operators =~ and !~
#
# There are three regular expression operators within Perl
# Match Regular Expression:     m//
# Substitute Regular Expression:    s///
# Transliterate Regular Expression:     tr///
