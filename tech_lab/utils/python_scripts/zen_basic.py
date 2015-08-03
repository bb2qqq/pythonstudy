# coding: utf-8

def make_sublist(raw_list, n):
    return [raw_list[i:i+n] for i in range(0, len(raw_list), n)]

# coding: utf-8
""" 一些常用的小工具 """

import importlib
import sys
from datetime import datetime

# short alias
dft = datetime.fromtimestamp

def reload_module_import_all(module_name):
    mod = reload(sys.modules['module_name'])
    globals().update(mod.__dict__)

def import_all_from_module(module_name):
    agent = importlib.import_module(module_name)
    globals().update(vars(agent))

def from_module_import_alias(module_name, var_name, alias):
    """ equal to from module import a as b """
    agent = importlib.import_module(module_name)
    globals()[alias] = vars(agent)[var_name]


def convert_str_to_num(target_str, round_flag=False, float_flag=False, int_flag=False):
    """ 转换浮点或整数形式的字符串到数字。
        round_flag设为True开启四舍五入
        float_flag为True返回浮点数
        int_flag为True返回整数部分
        如果int_flag和float_flag同时开启，返回字符的整数部分。
    """
    target_str = str(target_str)

    if '.' in target_str:
        result = float(target_str)
        str_type = 'float'
    else:
        result = int(target_str)
        str_type = 'int'

    if round_flag and str_type == 'float':
        result = round(result)

    if float_flag:
        result = float(result)

    if int_flag:
        result = int(result)

    return result


def n_pos_with_m_status(status_list, r, cur_combo=()):
    """ 有r个位置，每个位置有若干种状态,  每个位置的状态集是相同的。
        一个位置编号+该位置状态=该位置属性，
        找出所有不同位置属性的组合
        这是我写的第一个recursion函数，
                                        Tue Jul  7 17:59:34 CST 2015
    """
    r -= 1
    temp_list = []
    for i in status_list:
        if r > 0:
            temp_list = temp_list + genius_recursion(status_list, r, cur_combo + (i,))
        else:
            temp_list.append(cur_combo + (i,))
    return temp_list

