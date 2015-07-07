# coding: utf-8
def single_generator():
    """返回一个generator, 这个generator里只有1个value, 它的value就是yield返回的东西，
       可以是int,str,或者像此处一样，是一个generator
    """
    yield (i for i in range(5))

def nested_generator():
    """ 返回一个generator, 这个generator里的每个value本身又是一个generator"""
    for i in range(3):
        yield (i for i in range(5))

SIGNAL = 0
def toy_generator():
    yield 1
    for i in range(3):
        yield (i for i in range(5))
    if SIGNAL:
        yield 0
