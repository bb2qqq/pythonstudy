### 将任意字符串变成全局变量

      target_string = raw_input()
      command_1 = 'global %s' % target_string
      exec(command_1)
      globals()[target_string] = self



### 在全局变量中执行字符串命令
exec默认是在locals()变量环境里执行语句，如果想要在全局变量环境里执行的话

你需要使用 `exec 'my_command' in globals()`  
如果需要在本地和global的混合环境里执行命令，你使用`exec 'my_command' in globals(), locals()`  

[相关讨论](http://stackoverflow.com/questions/2083353/cannot-change-global-variables-in-a-function-through-an-exec-statement)
[官方文档](https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement)


### 查看一个OBJ的代码依赖关系
    import traceback
    # inside something
    for i in traceback.extract_stack:
        print i


### 查看一个变量是否是函数
    hasattr(var, '__call__')


### 反转变量True False属性
    a = "Hi"
    a = not a
    a
    False
    a = not a
    a
    True


### 小心浮点数
在python2.7里，你指定一个值，st=0.7999999999999，你调用该值，得到0.7999999999999， 你print它， 你得到的是。。`0.8`


### 让你的程序运行指定的时长
    import signal
    import sys

    def terminate_func(*args, **params):
        # do your final things here before exit
        sys.exit(0)

    signal.signal(signal.SIGALRM, terminate_func)
    signal.alarm(100)   # after 100 seconds of running, execute terminate_func

> The running time isn't precise, like signal.alarm(100) could use 100.00013332 seconds.

### python2做除法时直接求浮点数
    >>>from __future__ import division
    >>>2/3
    0.6666666666666666
    >>>3/3
    1.0

> 在python 3中，此种除法方式是default行为

### 将url中特殊字符(% + alphanum表示的那些字符)进行转换
    import urllib
    converted_str = urllib.unquote(raw_url_str)

### 将一个大列表以n的跨度切割成若干小列表
    new_list = [raw_list[i:i+n] for i in range(0, len(raw_list), n)]

### 使用文件名字符进行from m import *操作
    agent = importlib.import_module(module_name)
    globals().update(vars(agent))

### 将一个python数据转换成json格式
    import json
    converted_json_data = json.dumps(raw_python_data)

### 让一个python文件打印自己的所有内容！
    print open(__file__).read()

### 快速将字符串解析成datetime对象
    from dateutil import parser
    datetime_obj = parser.parse(datetime_str, fuzzy=True)

> fuzzy=True会开启模糊模式，忽略一些parser不能识别的字符

### 在cent-OS上给python安装mysql模块
    # First you shall install mysql-devel, such as:
    yum install mysql-devel
    # Then install mysql module in python
    pip install mysql


### 快速打印格式化的当前年月日和时分秒
    import time
    time.strftime('%F %T')
    # %F 是年月日在time模块里的快捷表示，%T是时分秒的快捷表示

### 一句话反转字典键值对
    inv_map = {v:k for k,v in my_dict.items()}

### 简单粗暴解决各类utf-8编码问题

    # coding: utf-8
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")


### 查看当前python进程使用的内存大小
    import resource
    mem_usage = resource.getrusage(resource.RUSAGE_SELF)
    print mem_usage.ru_maxrss

    # OSX 下的单位是byte, 而Linux下的单位是kilobyte
    # 将RUSAGE_SELF 换成 RUSAGE_CHILDREN 来查看子进程的内存占用

### 判断一个对象的大小
    # 方法1
    import sys
    sys.getsizeof(object[, default])

    # 方法2
    object.__sizeof__()

### 判断一个对象是否是iterable
    if hasattr(my_obj, '__iter__')


### 获得当前文件路径
    import os
    os.path.dirname(os.ptah.abspath(__file__))      # 文件存储路径
    os.getcwd()                                     # 当前所在的执行路径

### 检测一个对象是否是字符串(包括普通字符和unicode字符)

    isinstance(obj, basestring)

### Write several statement in a line.(using ;)

    salary=1000; bonus=1200; print salary + bonus


### Log detailed error info without exit python process

    import traceback
    import sys
    try:
        eval('Your Arbitary Code here')
    except:
        print 'This is diy error log'
        print traceback.format_exc()
        print sys.exc_info()

> SyntaxError can only be caught when the code executed in eval or exec. Try remove eval and quote, you'll know what I mean.

### Convert python data structure to json

    import json
    json_data = json.dumps(my_dict)


### print ###

* To print without carriage, you add a comma after what you wanna print

    print 'my string',


### Arithmatic operation ###

* convert a string coded in base-n system into decimal number

      int(str, base_n)
      e.g: int('0xAE', 16)



## DATA STRUCTURE ##


#### SET OPERATION ####

    UNION               s | t           #  all elements in s and t, except duplicate
    INTERSECTION        s & t           #  elements that are in s and t
    DIFERENCE           s - t           #  element in s but not in t
    SYMMETRIC_DIFFER    s ^ t           #  equal to (s - t) | (t - s), means that element in t or s that are not appeared in both set



* if List_A exists, iter over List_A, otherwise iter over List_B

        for i in List_A or List_B:
            print i

* Formate Year/Month/Day without 0 padding

        import datetime
        "{dt.year}{dt.month}{dt.day}".format(dt=datetime.datetime.now())

* delete one item from a dict

        my_dict.pop(key, default_value)

>   This will delete the key-value pair if key in my_dict, otherwise defualt_value will be returned, so you won't get an error when key isn't in my_dict

