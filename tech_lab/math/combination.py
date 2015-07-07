# coding: utf-8
from math import factorial
import itertools

def make_tuple(objects, attributes):
    """ 传入两个包含若干元素的iterator, 将该两组元素所有可能的交叉组合的tuple以list形式返回  """
    tuple_list = []
    for obj in objects:
        for attr in attributes:
            tuple_list.append((obj, attr))
    return tuple_list

def combinate(elements, unit_range):
    """ 根据elements里的元素，返回不重复的所有unit_range个元素的组合 """


def find_tuple_combinations(objects, attributes, n):
    """ 有若干个单位，每个单位有若干种状态，用若干个单位做成一个组，在不重复遍历的情况下将所有组合找出来 """
    # 将问题转换成x个元素y个一组有多少种组合方式的问题
    all_elements = find_tuple_combinations(objects, attributes)
    tuple_combinations =  combinate(all_elements, n)


def combination_checker(item_nums, com_range):
    return factorial(item_nums) / (factorial(com_range)*factorial(item_nums-com_range))


def default_combination_checker(iterable, r):
    return len(itertools.combination(iterable, r))


def official_combination(iterable, r):
    """ official python combination realization """
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r) 
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n  - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def n_pos_with_m_status(pos_list, status_list):
    """ 有n个位置，每个位置有m种状态,  每个位置的状态集是相同的。
        一个位置编号+该位置状态=该位置属性，
        找出所有不同位置属性的组合
    """


status_list = ['empty', 'wall', 'can']


def genius_recursion(L, r, cur_combo=()):
    r -= 1
    temp_list = []
    for i in L:
        if r > 0:
            temp_list = temp_list + genius_recursion(L, r, cur_combo + (i,))
        else:
            temp_list.append(cur_combo + (i,))
    return temp_list

for i in status_list:
    for j in status_list:
        for k in status_list:
            for m in status_list:
                for n in status_list:
                    print i, j, k, m, n
