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

