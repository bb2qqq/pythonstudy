#__metaclass__ = type
import random

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

class TestIterator:
    value = 0
    """ To make an iterator, you must have a 'next' method in your object """

    def next(self):
        self.value -= 1
        if self.value <= -10: raise StopIteration  # StopIteration will simply stop the iteration when a for loop reaches this triger condition, without prompt out an alarming error

    def __iter__(self):
        return self

def check_index(key):
    if not isinstance(key, (int, long)): raise TypeError('Tenemos que cargar muchos pesados')
    if key<0: raise IndexError('Tencent is a bully company')


class BaseItem(object):
    def __getitem__(self, key):
        try:
            return self.key
        except:
            return 'haha, hehe, heihei'

    def __setitem__(self, key, value):
        self.__dict__[key] = value

class TestClassMagic(object):
    """When del self.egg, we'll call self.recycle *=2, when call self.recycle *2, we'll triger __setattr__, thus self.recycle would become some random value, wow """
    egg = 'chicken'
    recycle = '---waste---'

    def __setattr__(self, name, value):
        value = random.choice(['pato', 'zepra', 'neto', 'gigi', 'monja', 'palillo'])
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        self.recycle *= 2



class ClassMagicMethod(object):

    """ Seems __getattribute__ has priority over __getattr__ """

    egg = 'chick'                           # use self.egg we can call this, and you can't define self.egg = blahblah in this line

    def __getattr__(self, name):
        return 250

    def __getattribute__(self, name):
        if 't' in name:                                         # Even call object.__dict__ will triger this !
            return "At the seventh day, god makes human beings"
        else:
            return object.__getattribute__(self, name)

    def show_egg(self):
        print self.egg

class Mini(object):
    @property
    def t(self):
        """ ahhhh """
        return 0

class MiniNew(object):
    t = property(doc='This is a doc')

class TestProperty(object):
    def __init__(self):
        self.val = 0
        self.rand_val = 0
    @property
    def x(self):
        """ hack me """
        self.rand_val =  random.choice(xrange(50000))
        another_rand = random.choice(xrange(50000))
        return another_rand

    @x.setter
    def x(self, value):
        self.val += value * self.rand_val
        print 'Test setter'
    @x.deleter
    def x(self):
        print 'Test deleter'

class TestPropertyNew:
    def __init__(self):
        self.val = 0
        self.rand_val = 0

    def get_x(self):
        """ hack me """
        self.rand_val =  random.choice(xrange(50000))
        another_rand = random.choice(xrange(50000))
        print another_rand

    def set_x(self, value):
        self.val += value * self.rand_val
        print 'Test setter'

    def del_x(self):
        print 'Test deleter'

    x = property(get_x, set_x, del_x, '''How to view the property doc?''')

class MiTesoro(object):
    def __init__(self):
        self.money = 0
        self.wisdom = 0
    def get_wealth(self):
        self.money += 1
        self.wisdom *= 1.001
        return self.money
    def set_wealth(self, value):
        self.money /= 2
        self.wisdom -= 2
    def del_wealth(self):
        print 'Are you sure that you want to do that?'
        answer = raw_input()
        if answer == 'yes':
            print 'Sorry, but it seems that you can\'t do it for now, don\'t be hurry lo'
        else:
            print 'Miewwww'
#    property(doc='''momoma''')
    wealth = property(get_wealth, set_wealth, del_wealth)

class StaClass:
    def smeth():
        print 'This is a static method'
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a class method of', cls
    cmeth = classmethod(cmeth)

class NoEsCero:
    def __init__(self, sig=0):
        self.sig = sig
    def __nonzero__(self):
        if self.sig:
            return 1
        else:
            return 0

class ArithmeticSequence:
    def __init__(self, start=0, step=1, magic_sig=0):
        self.start = start
        self.step = step
        self.changed = {}
        self.magic_sig = magic_sig

    def __getitem__(self, key):

        check_index(key)

        try: return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value

    def __len__(self):
        if self.magic_sig == 0:
            return len(self.changed)
        else:
            return 1997

    def __delitem__(self, key):
        print 'As we are a developed country, we should cherish our datas, instead of throw it into dustbin like you do. Shame on you!'

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
