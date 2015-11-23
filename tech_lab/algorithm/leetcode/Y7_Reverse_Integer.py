# coding: utf-8
"""

Link: https://leetcode.com/problems/reverse-integer/

Description:
    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

"""
# 在python里，这又是很简单的一个问题，先string化，再把字符的顺序变成逆序就好了
# 更粗暴是字符变列表，列表reverse一下，再变成字符，再转成int就好。
# 唯一需要额外考虑的是负号

class SolutionAccepted_1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        1032 / 1032 test cases passed.
        Status: Accepted
        Runtime: 68 ms
        Submitted: 0 minutes ago

        """
        str_x = str(x)

        # 处理负号
        if str_x[0] == '-':
            str_x = str_x[1:]
            negative_symbol = '-'
        else:
            negative_symbol = ''

        L = list(str_x)
        L.reverse()
        reversed_str = ''.join(L)
        final_str = negative_symbol + reversed_str
        result = int(final_str)

        # 这两个值分别是负2的31次方和正2的31次方，出题者说，我的Int是32位精度的哦
        if not -2147483648 <= result <=2147483647:
            return 0
        return result

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        不使用list reverse方法的solution
        """
        str_x = str(x)
        # 处理负号
        if str_x[0] == '-':
            str_x = str_x[1:]
            negative_symbol = '-'
        else:
            negative_symbol = ''

        L = list(str_x)
        for index, value in  enumerate(str_x):
            L[-(index + 1)] = value
        reversed_str = ''.join(L)
        final_str = negative_symbol + reversed_str
        result = int(final_str)

        # 这两个值分别是负2的31次方和正2的31次方，出题者说，我的Int是32位精度的哦
        if not -2147483648 <= result <=2147483647:
            return 0
        return result
