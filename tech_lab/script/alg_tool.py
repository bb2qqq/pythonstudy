# coding: utf-8
""" 本脚本文件用于存放进行算法计算的小工具 """
def smallest_value_diff(L):
    """ 找出目标列表中差值最小的两个数字的组合, 此方法算法复杂度较高 """
    cur_diff = float('inf')
    result = None
    for n1 in L:
        for n2 in L:
            if n1 != n2:
                i1 = L.index(n1)
                i2 = L.index(n2)
                diff = abs(n1 - n2)
                if diff < cur_diff:
                    cur_diff = diff
                    result = [(n1, n2, i1, i2)]
                elif diff == cur_diff:
                    result.append((n1, n2, i1, i2))
    return result
