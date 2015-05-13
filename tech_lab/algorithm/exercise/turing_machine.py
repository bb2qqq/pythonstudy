# coding: utf-8
""" 本文件用来展示并非所有的数学声明都能在有限步骤内证明其真伪性"""
import random

our_statement = "给定一个图灵机Z, 和输入Z, 在有限的时间里它会停止。"

# 我们先假定这个声明在有限步骤内是可以证明真假的

# 就是说图灵机Z使用输入Z, 在有限时间里要么停止，要么不停止
# 我们有种方法可以在有限时间内发现它停不停止
# 这种方法就是Statement_examiner

def Statement_examiner(Turing_machine, input_, result=None):
    """ Statement_examiner 会取一个图灵机的代码和输入I作为自己的输入，
        并判断该图灵机在输入I情况下是无限循环还是有限循环。
    """
    if result == 'finite':
        return 'finite'
    elif result == 'infinite':
        return 'infinite'
    else:
        return random.choice(['finite', 'infinite'])


def Z(Turing_machine, result=None):
    """ 图灵机Z的规则是，接收一个图灵机代码作为输入，
        将这个图灵机的代码分别作为图灵机代码和输入交由Statement_examiner处理
        如果Statement_examiner返回的结果是yes, 图灵机Z进入无限循环
        反之，图灵机Z停止
    """
    examine_result = Statement_examiner(Turing_machine, Turing_machine, result)
    if examine_result == 'finite':
        print examine_result
        return 'infinite'
    elif examine_result == 'infinite':
        print examine_result
        return 'finite'
