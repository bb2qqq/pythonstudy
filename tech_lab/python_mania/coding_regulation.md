### 代码规范的目的
**Guido的一个重要洞见是，比起被写而言，代码被读得更多。**  
**提升代码的可读性可以提升项目组里每个人的工作效率。**  
**本编码规范的目的在于改善 Python 代码的可读性、使不同程序员书写的的 Python 代码保持一致性。**

<br>
### 缩进

**每级缩进使用4个空格**

** 不要混合使用tab和空格进行缩进 !**


对连续的行（一行展开成多行）排版时，要么将内容与圆括号/方括号/花括号对齐，要么使用悬挂式缩进。  
使用悬挂式缩进时请注意：第一行不能带任何参数，而之后的行必须清晰地体现它们是连续的行。

      Yes:

      # 和开口定界符对齐
      foo = long_function_name(var_one, var_two,
                               var_three, var_four)

      # 悬挂式缩进应该加一个缩进等级
      foo = long_function_name(
          var_one, var_two,
          var_three, var_four)

      # 加入额外的缩进来区分连续的行与其他内容。（此为悬挂式缩进)
      def long_function_name(
              var_one, var_two, var_three,
              var_four):
          print(var_one)


      No:

      # 如果之后的内容不与第一行定界符对齐时，第一行内不能带参数！
      foo = long_function_name(var_one, var_two,
          var_three, var_four)

      # 悬挂式缩进的缩进等级不能很好地把连续行与其它内容区分开来。
      def long_function_name(
          var_one, var_two, var_three,
          var_four):
          print(var_one)

> 调用函数或方法时，最尾部的闭合定界符需要紧跟最后一个参数。


当 if 语句的判断条件非常长，以至于需要用多行来写下它们时。  
我们需要注意的是，if 语句天然的要求条件之后的执行语句有4个空格的缩进等级,  
这会导致连续缩进的行与其他内容产生视觉冲突。  
以下是两种缓解这种冲突的方式(我个人偏向于第1种):


      # 在条件行缩进加入额外的缩进等级
      if (this_is_one_thing
              and that_is_another_thing):
          do_something()

      # 加一行注释，这使得在编辑器里可以看到视觉的区分效果
      if (this_is_one_thing and
          that_is_another_thing):
          # 因为两个条件都满足，我们可以继续
          do_something()
          

      结尾闭合的定界符(圆括号/方括号/花括号)可以与多行结构里最后一行的第一个非空白字符对齐， 如：

      my_list = [
          1, 2, 3,
          4, 5, 6,
          ]

      result = some_function_that_takes_arguments(
          'a', 'b', 'c',
          'd', 'e', 'f',
          )


      或者可以与该结构里第一行的第一个非空白字符对齐， 如：

      my_list = [
          1, 2, 3,
          4, 5, 6,
      ]

      result = some_function_that_takes_arguments(
          'a', 'b', 'c',
          'd', 'e', 'f',
      )


### 行的排版

**每行代码长度最好保持在79字符以内。**
  
虽然现代的显示屏和terminal更先进，能够显示更多的字符，但使用PEP8里推荐的每行79字符的限制仍有以下好处：  

1. 使得多窗口并排浏览代码更加方便  
2. 可以提醒你代码不够简洁，需要重构  

> 在实践中，有一些公司根据自己的需要将限制放宽到（80-100）个字符。



包裹长行的最佳方法是使用内置数据结构本身的圆括号，方括号或花括号。  
长表达式也可以用一对额外的圆括号包裹起来( 注意在二进制运算符之后换行，而不是在它之前 )。  
例：


      class Rectangle(Blob):

          def __init__(self, width, height,
                       color='black', emphasis=None, highlight=0):
              if (width == 0 and height == 0 and
                      color == 'red' and emphasis == 'strong' or
                      highlight > 100):
                  raise ValueError("sorry, you lose")
              if width == 0 and height == 0 and (color == 'red' or
                                                 emphasis is None):
                  raise ValueError("I don't think so -- values are %s, %s" %
                                   (width, height))
              Blob.__init__(self, width, height,
                            color, emphasis, highlight)


当以上的方法都不可用的时候，你用`\`来表示行之间的连续关系，如：

      with open('/path/to/some/file/you/want/to/read') as file_1, \
           open('/path/to/some/file/being/written', 'w') as file_2:
          file_2.write(file_1.read())
      (See the previous discussion on multiline if-statements for further thoughts on the indentation of such multiline with -statements.)
      (回顾前面关于if语句多行连接的讨论，想一下在这个with语句里该如何缩进)
      (PS: 我感觉这儿得加注释来进行视觉区分了，如 # 文件打开完毕)

> 在换行符`\`后不要有多余的空格：否则在使用换行符`\`的时候会导致错误发生。


* 顶级函数与类之间用两个空行分隔。  

* 类方法之间用一个空行分隔。  

* 你可以使用额外的空行来分隔相关的函数群。  

* 在函数中使用空行时，请谨慎地用于表示一个逻辑段落。


#### 模块引用

每一个模块应该尽量用单独一行导入，如：

    import os
    import sys

但这样写也是可以的：

    from sbuprocess import Popen, PIPE

模块引用通常放在文件的顶部，仅在模块注释和文档字符串之后。

import模块的先后顺序如下：  

1. 标准库
2. 相关第三方库
3. 本地库

在每组导入之间应该以空行间隔

** ！ 避免通配符引用 ( from <module> import * ) **

通配符引用会使得读者不清楚在命名空间里到底有哪些变量名。




### 空格使用

** 避免如下的多余空格：**

* 紧挨着圆括号、方括号和花括号的空格：

      Yes: spam(ham[1], {eggs: 2})
      No:  spam( ham[ 1 ], { eggs: 2 } )


* 在逗号、分号或冒号前：

      Yes: if x == 4: print x, y; x, y = y, x
      No:  if x == 4 : print x , y ; x , y = y , x


* 冒号`:`会有一种特殊应用场景--列表切分, 此时它应被考虑为优先度最低的运算符。  
在此情境下，应确保对每个冒号使用相同多的空格。  
如果参数被省略的话，空格也应该被省略。

      Yes:

      ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
      ham[lower + offset : upper + offset]

      No:

      ham[1: 9], ham[1 :9], ham[1:9 :3]
      ham[lower + offset:upper + offset]
      ham[lower : : upper]
      ham[ : upper]

* 函数调用参数的开括号前

      Yes: spam(1)
      No:  spam (1)

* 索引或切片的开括号前

      Yes: dct['key'] = lst[index]
      No:  dct ['key'] = lst [index]

* 在赋值 (或其他) 运算符周围的用于和其他语句对齐的超过一个的空格：

      Yes:
      x = 1
      y = 2
      long_variable = 3


      No:
      x             = 1
      y             = 2
      long_variable = 3

** 其他建议: **

* 在字典里紧跟key的冒号`:`后加一个空格；在分隔字典，元组和列表元素的逗号`,`后加一个空格：
      
      Yes:
      age_ref = {'Mike': 5, 'Tom': 8, 'Mary': 10}
      fruits = ['apple', 'banana', 'orange']
      couple_one = ('Lucy', 'Mann')



* 始终在这些二元运算符两边放置一个空格:
 
  赋值符 ( = )  
  增量赋值符 ( +=, -= 等 ),  
  比较符 ( ==, <, >, !=, <>, <=, >=, in, not in, is, is not ),  
  布尔符 ( and, or, not ).

* 当运算中会用到拥有不同优先级的运算符时，考虑在运算优先度最低的运算符周围加上空格：

      Yes:

      i = i + 1
      submitted += 1
      x = x*2 - 1
      hypot2 = x*x + y*y
      c = (a+b) * (a-b)


      No:

      i=i+1
      submitted +=1
      x = x * 2 - 1
      hypot2 = x * x + y * y
      c = (a + b) * (a - b)



* 在对函数定义默认参数值和向函数里传指定参数时，不要在`=`号附近使用空格

      Yes:

      def complex(real, imag=0.0):
          return magic(r=real, i=imag)
      No:

      def complex(real, imag = 0.0):
          return magic(r = real, i = imag)

> python3 的函数定义支持Function Annotation，因此关于python3函数参数定义的PEP-8标准也发生了变化

* 不推荐使用复合语句（多条语句写在一行里）

      Yes:
          if foo == 'blah':
              do_blah_thing()
          do_one()
          do_two()
          do_three()

      Rather not:
          if foo == 'blah': do_blah_thing()
          do_one(); do_two(); do_three()

* 虽然有时可以在 if/for/while 的同一行跟一小段代码，但绝不要对多条子句也这样做。  
 也避免折叠这样的长行。

      Rather not：
      
          if foo == 'blah': do_blah_thing()
          for x in lst: total += x
          while t < 10: t = delay()


      Definitely not：
      
          if foo == 'blah': do_blah_thing()
          else: do_non_blah_thing()

          try: something()
          finally: cleanup()

          do_one(); do_two(); do_three(long, argument,
                                       list, like, this)
                                       
          if foo == 'blah': one(); two(); three()

### 注释

**和代码不一致的注释比没注释更差。当代码修改时，始终优先更新注释！**

<br>
注释应该是完整的句子。

如果英文注释是一个短语或句子，首字母应该大写，  
除非它是一
个以小写字母开头的标识符 (永远不要修改标识符的大小写)。

如果注释很短，可以省略末尾的句号。  
注释块通常由一个或多个段落组成，段落是由完整的句子构成的，每个句子应该以句号结尾。  
你应该在结束语句的句点 (a sentence-ending period) 后使用两个空格。

非英语国家的 Python 程序员：请用英语书写你的注释，除非你120% 的确信代码只会被懂你母语的人所阅读。

<br>
**注释块**

  注释块通常应用于跟随其后的一些 (或者全部) 代码，并和这些代码有着相同的缩进层次。  
  注释块中每行以 '#' 和一个空格开始。  
  注释块内的段落以仅含单个 '#' 的行分割。

**行内注释**

节制的使用行内注释。

一个行内注释是和语句在同一行的注释。  
行内注释应该至少用两个空格和语句分开。  
它们应该以一个 '#' 和单个空格开始。

行内注释不是必需的，事实上，如果说的是显而易见的事，还会使人分心。不要这样做：

        x = x + 1                # 增加x的值

但是有时，这样是有益的:

        x = x + 1                # 边界值补偿


### 文档

<br>
** 写文档是为了增强代码的可读性 **

<br>
Docstring(文档)是紧挨着模块，类，函数，方法定义下的第一个字符串, 以三个双引号`"""`包裹。

模块包(package)的Docstring请放在`__init__.py`文件的模块文档里,  
通常情况下所有的模块都应该有文档，    
所有会被引用的类和函数应该有文档，  
类里的所有公共方法(包括__init__构造方法)也应该有文档。   
  
对于类里的非公共方法，你应该在方法定义下写一个注释，介绍用途。

* 单行文档

  单行文档是在代码情况很简单的情况下使用的，他们应该保持在1行内（小于79个字符）， 例：

      def kos_root():
          """返回KOS root 文件夹的路径。"""
          global _kos_root
          if _kos_root: return _kos_root

  **注意：**
    
  单行文档的所有引号和文本应该在同一行内。  
  在单行文档之前和之后没有空行。  
  单行文档应该是一个以句号结尾的句子，它用来指示一个函数或方法作为一个命令所产生的效果，  
  如`做这件事`，`返回那个结果`, 而不是一个描述，如：`将满足xxx条件的路径返回到...`

  单行文档不应该像签章一样，重申一个函数或方法的参数(这些信息可以通过hepl()函数得到)，**不要写这样的文档**：

      def function(a, b):
          """function(a, b) -> list"""

  上述类型的文档只对 C 语言函数是合适的（比如内置函数）。  
  然而返回值并不能被python的内省机制发现，所以它应该被提到，**理想的单行文档如下**：

      def function(a, b):
          """Do X and return a list."""
      (此处的`Do X` 应被替换为你的函数具体做的事情)


* 多行文档

  多行文档包含一行和单行文档相同的摘要行，在它之后应该加一个空行，空行后是一段更详细的描述。  
  你可以用自动化工具来生成摘要行，重要的是它应该能放得进一行并且用空行与其余文档部分隔开。  
  摘要行可以与文档开头的三个引号`"`在同一行或者另起一行。  
  整个文档应该同文档开头的三个引号`"`缩进相同的等级。  
  
  <br>
  脚本的文档应该像一个关于它的`使用方法`，  
  当脚本不正常运行或是缺少参数的时候被打印出来，  
  也可以加一个 -h 选项，用来打印该帮助文档。  
  这个文档应该将脚本里的环境变量，命令行语法，函数，和相关文件记录下来。  
  使用方法的信息可以非常的详尽（长达数屏都可以），  
  并且足够让一个新用户正确地使用相关命令。  
  此外，还应附上一个简洁的额外选项和参数的对照表，以供经验丰富的使用者参考。

  <br>
  模块的文档里应当列出该模块输出的所有的类，exception, 和函数(以及其他对象)，  
  每个对象跟一条一行的简介。  
  一般而言，模块文档里给出的简介信息要比所介绍的对象内部文档的摘要信息要少。  
  一个模块包的文档应当列出它所输出的模块和子模块包的信息。  

  <br>
  函数或方法的文档应当概述它的行为，  
  并记载它的参数，返回值，exception, 副作用，和使用限制的具体信息。    
  额外的参数应当被指出来，并且应当说明关键词参数是否是接口的一部分。  

  <br>
  类的文档应当概述它的行为，将所有的公共方法和实例变量列举出来。  
  如果这个类有为其子类专门设计的接口，该接口在文档中的说明应当单独列在一边。  
  在类的文档的最后加一个空行，以将它与类的第一个方法隔离开。  
  独立的方法的具体信息应当被记录在它自己的文档里。  

  如果一个类是其他类的子类，并且它的行为大多数继承自它的父类，  
  它的文档应当提到这一点并且将差异概述出来。  
  使用动词`覆盖(override)`来表示子类的方法替换了父类的方法，并且不会调用父类方法；
  使用动词`扩展(extend)`来表示子类方法会调用父类方法（在子类方法行为的基础上）


<br>
文档可以用`object.__doc__`的方法获得，也会显示在`help(object)`返回的信息里，有助于代码阅读者更好的理解代码。

以下是文件`sample.py`的内容：

      ------ 代码内容 ------

      # coding: utf-8
      """
        本模块用于展示如何在模块中使用文档.
        文档可以扩展多行，
        多行注释里最后一行的三个双引号应该单独占一行。
      """

      def sample_func():
          """ 展示用，返回None """

      class Sample(object):
          """  用于展示在类中使用Docstring 

               sample_method: 展示用类方法，返回None 
          """

          def __init__(self):
              """ 展示用，返回None """

          def sample_method(self):
              """ 展示用，返回None """


      ------ 命令行演示 ------

      >>> import sample
      >>> print sample.__doc__
      本模块用于展示如何在模块中使用文档.
      文档可以扩展多行，
      多行注释里最后一行的三个双引号应该单独占一行。
      >>> help(sample.Sample.sample_method)
      Help on method sample_method in module sample:

      sample_method(self) unbound sample.Sample method
          展示用，返回None
      (END)


### 命名规范


python包名应该是简短的，全小写的名字，不推荐使用下划线`_`, 例：`logics`  
模块名称应当使用全小写的单词，如果使用下划线`_`可以提高可读性的话，可以使用， 例：`run_timer.py`。  
类名应当使用首字母大写单词串，例：`RewardGacha`。  
函数名应当使用小写单词，使用`_`分隔单词来提升可读性，例：`reload_config`。      
**方法命名，实例变量命名，全局变量名命名与函数命名规则相同**。   
常量通常在模块级别被定义，使用全大写并用`_`分隔单词，例：`MAX_OVERFLOW`。

> 在你不想被其他模块引用的全局变量名前加`_`, 对于那些私有的方法名和实例变量你也这样做。  
> **让你的命名在合理的前提下尽量的简短。太长的命名会影响代码整体的可读性。   
> 在python各类标准库的命名里，绝大部分命名都在三个单词以内。**  
> 相关讨论链接: http://stackoverflow.com/questions/16920835/what-is-the-maximum-length-for-an-attribute-name-in-python

对实例的方法，总是用`self`做第一个参数名。  
对类方法，总是用`cls`做第一个参数名。  
如果函数名称同python保留关键字冲突，在名称后加一个下划线比改写名称好。  
如`class_`比`clss`好。当然，能使用同义词代替是更好的。  

<br/>
在定义类时，总是考虑它里面的方法和变量是否应该被公开。  
如果你有疑问，把它们设成非公开方法和非公开变量。  
因为将一个私有属性公开化比将一个公开属性私有化要容易得多。  


公开属性是那些你认为谁都能用的，并且能够保证不会做出向后不兼容的改变的属性。  
而你不需保证私有属性不会变动，你甚至可以根据你的需求删除它。  

> 注意，PEP原文里`私有`一词用的是`non-public`，因为在python里没有属性是真正私有的。



** 特殊命名 **

`_single_leading_underscore`(单前导下划线): 弱的内部使用标志。  
例如 `from M import *`不会导入以下划线开头的对象

<br>
`single_trailing_underscore_`(单后置下划线): 用于避免与python自带关键词冲突。  
例如： `Tkinter.Toplevel(master, class_='ClassName')`

<br>
`__double_leading_underscore`(双前导下划线): 当用于命名 class 属性时，会触发名字改编。  
例如，在类 `FooBar` 中，`__boo`属性的名字 会变成 `_FooBar__boo`

<br>
`__double_leading_and_trailing_underscore__`(双前导和双后置下划线): "magic" 对象或属性。  
例如: `__init__`, `__import__`。 决不要发明这样的名字，仅按照文档中说明的那样使用他们。

<br>
当一个用 C 或 C++ 写的扩展模块，有一个伴随的 Python 模块来提供一个更高层(例如，更面向对象)的接口时，C/C++ 模块名有一个前导下划线 (如：`_socket`)。

> 关于魔法method的guide: http://www.rafekettler.com/magicmethods.html

** 需要避免的命名方式 **

不要使用小写的字母`l`, 大写的字母`O`, 大写的字母`I`做变量名。

> 当你很想使用小写的`l`做变量名的时候，使用大写的`L`代替


### 编程建议

* 当需要连接大字符串时，使用`''.join([str1, str2])` 而非 `str1 += str2`

* 与 None 值进行比较时，使用`is`或`is not`, 不要使用`==`或`!=`

* 多使用`is not`, 少用 `not is`, 因为前者的可读性更好。

      Yes:
      if foo is not None:

      No:
      if not foo is None:

* 在捕获异常时，尽可能写出明确的异常，而不是使用空的 'except:' 子句。  
例如使用：

      try:
          import platform_specific_module
      except ImportError:
          platform_specific_module = None

  当你需要使用空的`except`语句时，确定你能打印或者记录报错信息。  
例如:

        import traceback
        import sys
        try:
            import platform_specific_module
        except:
            print 'Print error info and continue running'
            print traceback.format_exc()
            print sys.exc_info()

  另外，对所有 try/except 子句，只使用 `try` 语句所必须的最少量代码。  
以避免再次掩饰其他bug。

      Yes:

          try:
              value = collection[key]
          except KeyError:
              return key_not_found(key)
          else:
              return handle_value(value)

      No:

          try:
              return handle_value(collection[key])
          except KeyError:
              #  这个except会同时捕获collection[key] 和 handle_value的 KeyError, 这样你就不知道错误是在哪一步发生的了。
              return key_not_found(key)


* 使用 `''.startswith()` 和 `''.endswith()` 代替字符串切片，来检查前缀和后缀。  
startswith() and endswith() 更清晰易读，也倾向于减少错误。例如：

        Yes: if foo.startswith('bar'):

        No:  if foo[:3] == 'bar':

* 对象类型的比较应该始终用 `isinstance()` 代替直接比较类型。

        Yes: if isinstance(obj, int):

        No:  if type(obj) is type(1):

* 检查一个对象是否是字符串时，谨记它也可能是 unicode 字符串！在Python 2.3及以上版本里，str 和 unicode 有公共的基类 basestring，所以你可以使用`isinstance(obj, basestring)`方法，例:

        >>> u'a' == 'a'
        True
        >>> isinstance(u'a', str)
        False
        >>> isinstance('a', str)
        True
        >>> isinstance(u'a', basestring)
        True
        >>> isinstance('a', basestring)
        True

* 对序列 (字符串 (strings)，列表 (lists)，元组 (tuples))，使用空序列作为False。

      Yes: if not seq:
           if seq:

      No: if len(seq)
          if not len(seq)

* 不要书写后置空白字符有特殊意义的文本字符串。这种后置空白字符在视觉上不可区分，并且有些编辑器会裁剪掉它们。

* 不要用 == 来将布尔值与 "True 或 False" 进行比较。

        Yes:   if greeting:

        No:    if greeting == True:

        Worse: if greeting is True:

* 当你的python文件里含有中文字符时，在文档顶部加入：`# coding: utf-8`

* 不要用分号`;`来结束一行

* 可以使用简短的列表推导(list comprehension)，但不要使用过长的列表推导, 当事情过于复杂时，使用for循环：

      Yes:
        result = []
        for x in range(10):
            for y in range(5):
                if x * y > 10:
                    result.append((x, y))

      No:
        result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]



* 编代码时应仅使用英文文符号，注意不要将中英文符号混淆使用  
  有效符号: `,` `:` `'` `"`  
  非法符号： `，` `：` `‘` `”`  


* 避免产生潜在的歧义

      考虑如下的代码:
      if not a and b:
          do something
 
      当你状态不好的时候，大脑有时会自动脑补为：
      if not (a and b):
          do something

      如果我们这样写就可以避免这样的潜在误解(推荐)。
      if b and not a:
          do something

      或者以一种稍微丑陋一点但更可靠的方式标识出来。
      if (not a) and b:
          do something




### 其他

本文提到的vim配置：

    " 将文件里原有的tab转化为8个空格，在编辑时，按一下tab，缩进4个空格
    set expandtab | set tabstop=8 | set shiftwidth=4 | set softtabstop=4

    " 将行末多余空格以灰色高亮显示
    autocmd FileType python highlight ExtraWhitespace ctermbg=grey guibg=grey
    autocmd FileType python match ExtraWhitespace /\s\+$/
    " 将每行超出79个字符的部分以红色高亮显示
    autocmd FileType python highlight OverLength ctermbg=red ctermfg=white guibg=#592929
    autocmd FileType python 2match OverLength /\%80v.\+/


本文参考的source:

    # PEP8
    https://www.python.org/dev/peps/pep-0008/

    # PEP 257
    https://www.python.org/dev/peps/pep-0257/

    # PEP8 中文翻译
    http://wiki.woodpecker.org.cn/moin/PythonCodingRule

    # Google python 编码规范
    http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

    # PEP-20(Zen of python)的示例
    http://artifex.org/~hblanks/talks/2011/pep20_by_example.html
