# coding: utf-8
import time
import datetime
import traceback
import random

### ALIAS
date_from_stamp = datetime.datetime.fromtimestamp

### DATAS
return_msgs = [
    "Ala Huak bar",
    "Nice toy!",
    "大侠饶命！",
    "Seca",
]

GLOBAL_VARS = vars()

class MagicBall(list):
    """ Mario·Luis·Garcia 送给自己的27岁礼物。
        Not implemented:
            __subclasses__  (Get all subclasses of new-style class)
            __truediv__
            __complex__
            __enter__
            __exit__(self, exc_type, exc_val, exc_tb)
    """


    def __new__(cls):
        cls.birth_stamp = time.time()
        cls.birth_datetime = str(date_from_stamp(cls.birth_stamp))
        cls.setattr_history = []
        cls.getattribute_history = []
        return super(MagicBall, cls).__new__(cls)

    def __init__(self, age_0='1988-11-11'):
        """ 给自己建立一个替身,  """
        # Assign attrs
        self._bool = 1
        self._value = 0
        self.age_0 = time.mktime(time.strptime(age_0, '%Y-%m-%d'))
        self.age_30 = self.age_0 + 30 * 31557600   # Scientific seconds in a year

        self.exam_stamp = time.time()
        self.instance_name = self.inspect_self_name()
        shadow_name = 's_' + self.instance_name
        self.str_to_global_var(shadow_name, self)
        print shadow_name

    ### TOOLS
    def type_responser(self, _input, **params):
        """当_input变量等于相应类型时， 返回**params里预设的相应responser的结果。
           如在params里传入default_R参数, 当基本数据类型缺少responser时，执行default_R
        """
        # 为基本类型数据建立map表
        type_mapper = {str: "str_R", int: "int_R", float: "float_R", bool: "bool_R",
             dict: "dict_R", list: "list_R", set: "set_R",}
        default_responser = params.get('default_R', self.surprise)
        for _type, responser in type_mapper.iteritems():
            if type(_input) == _type:
                actual_responser = params.get(responser, default_responser)
                if hasattr(actual_responser, '__call__'):
                    return actual_responser()
                else:
                    return actual_responser

        # 当input不在type_mapper指定的数据类型里时，执行surprise
        return self.surprise()

    def surprise(self):
        if random.random() < 0.5:
            return random.choice(return_msgs)
        return "Surprise!"

    def inspect_self_name(self, verbose=False):
        """查看当前instance的name, 只对简单的m = MagicBall()赋值语句里的m对象有效"""
        current_stacks_info = traceback.extract_stack()
        instance_name_stack = -3  # This value varies depend on the relationship between codes.
        filename, line_number, function_name, code_text = current_stacks_info[instance_name_stack]
        # code_text here is the statement where instance get initialized
        # We assume the simplest case `obj = MyClass()`.
        # !!! Caution !!! For statement like `obj1, obj2 = MyClass(), MyClass()`,
        # this name guessing technique will fail.
        instance_name = code_text.split('=')[0].strip()

        # Print debug infos
        if verbose:
            for i in current_stacks_info:
                print i
            print '\n\n'

        return instance_name

    def str_to_global_var(self, string, obj):
        """将传入的有效string变为全局变量，值为obj。
           TODO: 需要考虑string不是有效变量名的情况。
        """
        command_1 = 'global %s' % string
        exec(command_1)
        globals()[string] = obj

    ### Utils
    def get_current_age(self):
        delta_date = date_from_stamp(time.time()) - date_from_stamp(self.age_0)
        return str(round(delta_date.days/365.25, 2))
    ### ATTRIBUTES
    def __str__(self):
        """ Triggered when calling str(instance).
            If __str__ was not defined, but __repr__ was defined,
            str(instance) will return the value of ojb.__repr().
        """
        return '尼卜懂窝嘚傷苝(╯3╰)'

    def __unicode__(self):
        return unicode('ສະບາຍດີຊາວໂລກ', 'utf-8')

    def __nonzero__(self):
        """ Return value of this method will be the value of obj in `if obj` statement """
        self._bool ^= 1
        return self._bool

    def __len__(self):
        """ 返回按初始参数你活过的天数，如果已满30岁，返回30岁生日的日期(三十而立)"""
        time_length = time.time()
        if time_length > self.age_30:
            return 20181111
        else:
            return int((time_length - self.age_0) // 3600 // 24)

    def __repr__(self):
        """ 人们叫我夜礼服假面。
            String representation of an object in console.
        """
        return "Mario's 27th Birthday gift"

    def __hash__(self):
        """ 所有人的身份证号码是一样的！
            All the instances of MagicBall have the same hash value(returnde by hash(instance)).
           And they will be considered as the same key in any python dictionary, the same obj in a set.
        """
        return int('1'*32)

    def __dir__(self):
        """ 谢绝参观！
            This will be triggered by dir(instance).
            Without the interference of our own magic method,
            it will return a list of names of current instance's attributes.
            Now it returns what we specified below.
        """
        return ['Access Denied']

    ### ATTRIBUTE ACCESS
    def __getattr__(self, name):
        """ Called when doing attribute access and name is not instance's attribute.
            Will be override by __getattribute__ when both defined"""
        return self.surprise()

    def __setattr__(self, name, value):
        """ Triggered when attempting to assign values to instances's attribute.
            !!!WARNING!!! You should not use `self.name = value` in this method, it'll cause infinite loop.
            Instead, use self.__dict__[name] = value!!! You should not use `self.name = value` in this method, it'll cause infinite loop.
            Instead, use self.__dict__[name] = value

            * This runs precede __init__, so set attrs action in __init__ will be effect by this method.
            * If you wanna set attrs in the instance without inteference with this method, do them in __new__
        """
        self.setattr_history.append((name, value, time.time()))
        self.__dict__[name] = value

    def __delattr__(self, name):
        """ Triggered when an attribute is deleted.
            As the case in __setattr__,
            using `del self.name` here will cause infinite loop,
            please use `del self.__dict__[name] instead.
            But be aware, please make sure name in self.__dict__,
            because __delattr__ will be triggered when using `del self.not_exist_attr`
        """
        _input = raw_input("请输入删除密码： ")
        if len(set(_input)) > 30 and name in self.__dict__:
            del self.__dict__[name]
        else:
            print "领导说了，不让(yang4)删"


#    def __getattribute__(self, name):
#        """ Works only for new-style classes.
#            Called when trying to access any attributes of instance,
#            Will override __getattr__ when both defined.
#            It's easily to get an infinite loop when using __getattribute__,
#            In this discusion it said that __getattr__ is preffered:
#            http://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute
#
#        """
#        if name not in self.__dict__:
#            return self.__getattr__(name)
#        if name == '__dict__':
#            self.getattribute_history.append((name, time.time()))
#k            _input = raw_input("你shueishuei, 你为什么要查字典呐？")
#k            while not len(_input) == 2 and len(set(_input)) == 1:
#k                _input = raw_input("不对！老实交代！")
#k
#        return self.__dict__[name]


    ### COMPARISIONS
    def __eq__(self, _input):
        def str_R(t1=self, t2=_input):
            return len(t1) == len(t2);
        return self.type_responser(_input, str_R=str_R)

    def __ne__(self, _input):
        def bool_R():
            return random.choice([True, False])
        def int_R():
            return random.choice([3, 7, 42, 1028, 1103, 1111, 1988, 1997, 2018])
        default_R = "Big Sister is sucking you! You nasty comrade!"
        return self.type_responser(_input, bool_R=bool_R, int_R=int_R, default_R=default_R)

    def __lt__(self, _input):
        """ 一种谦虚的表现。"""
        return True

    def __le__(self, _input):
        """ 一种谦虚的表现。"""
        return True

    def __gt__(self, _input):
        """ 绝不骄傲自大。"""
        return False

    def __ge__(self, _input):
        """ 绝不骄傲自大。"""
        return False

    def __get__(self, instance, owner):
        self._value += 500
        return 5

    def __del__(self):
        """Cat has 9 lives."""
        print "哈哈，你删不掉我的，(*^__^*) 嘻嘻……"
        cat_name = "_cat_" + self.instance_name
        self.str_to_global_var(cat_name, self)


    def __call__(self):
        return self.surprise()


    # ARITHMETIC OPERATION
    def __neg__(self):
        return self.surprise()

    def __add__(self, obj):
        self._value /= len(repr(obj))
        return self._value

    def __sub__(self, obj):
        self._value **= len(repr(obj))
        return self._value

    def __mul__(self, obj):
        self._value -= len(repr(obj))
        return self._value

    def __floordiv__(self, obj):
        """Triggered by // """
        self._value *= len(repr(obj))
        return self._value

    def __div__(self, obj):
        self._value += len(repr(obj))
        return self._value

    def __pow__(self, other, *args):
        self._value //= len(repr(obj))
        return self._value

    # BINARY ARITHMETIC OPERATIONS
    def __lshift__(self, other):
        return self.surprise()

    def __rshift__(self, obj):
        return self.surprise()

    def __and__(self, obj):
        return self.surprise()

    def __xor__(self, obj):
        return self.surprise()

    def __or__(self, obj):
        return self.surprise()

    # TYPE CONVERSION
    def __oct__(self):
        print '暴力膜巴不可取'
        return '010'

    def __hex__(self):
        print self.surprise()
        return '0x10'

    def __int__(self):
        return int(self._value)

    def __long__(self):
        return long(self._value)

    def __index__(self):
        print "国安永远争第一"
        return 2


m = MagicBall()
class Dumb(object):
    """ww"""
    val = 'dumb'
