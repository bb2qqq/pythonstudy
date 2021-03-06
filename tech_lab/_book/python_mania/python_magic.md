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

