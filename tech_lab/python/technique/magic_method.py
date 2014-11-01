#__metaclass__ = type
import random

def check_index(key):
    if not isinstance(key, (int, long)): raise TypeError('Tenemos que cargar muchos pesados')
    if key<0: raise IndexError('Tencent is a bully company')


class ClassMagicMethod(object):

    def __getattribute__(self, name):
        if 't' in name:
            return "At the seventh day, god makes human beings'

    def __getattr

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
