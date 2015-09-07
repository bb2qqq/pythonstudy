# coding: utf-8
"""
Link: https://leetcode.com/problems/excel-sheet-column-number/

Description:
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""

# 我首先想到的是，这是实现一个自定义的26进制到10进制转换。没错，就是这样的。
# 这个题目隐藏的意思就是这样。
# 那么，先创建一个value表，将A-Z分别与相应的10进制value对应。
# 接下来，我们需要创建一个规则，这个规则实际上就是 N 进制的规则。
# 即在 N 进制的一个符号表达式里， 第 -i 位上的符号 X 表示的值为 X 乘以 N 的 i-1 次方
# 如 153 在10进制里, 5 是第 -2 位，其值为 5*(10**(2-1)) = 50
#                                                                   2015-08-27 12:44

# 在python列表里，符号 X 在表达式 E 里的逆序位置我们可以用 E.index(X) - len(E) 来表示

# 我仔细看了下，这个和N进制还不一样。。。。。。。那么之前的推断是完全错误了。。。
#                                                                   2015-08-27 13:02

# 其实并没有完全错误，题设里的转化法实际上是一种没有 0 的进制表达法。
# 而 0 乘以任何数都为0， 一个没有0的进制使用我们在 08-27 12:44 时总结出来的那套转换方法，是完全没有问题的。
# Problem solved!
#                                                                   2015-08-27 17:22

class Solution(object):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_value_dict = {}

    for i,j in zip(alphabet, range(1,27)):
        alpha_value_dict[i] = j

    def BaseN_to_base10(self, expression, convert_dict):
        expr_length = len(expression)
        total_value = 0
        base_length = len(convert_dict)

        for index, n in enumerate(expression):
            revert_order_of_n = index - expr_length
            value_n = convert_dict[n] * (base_length**(abs(revert_order_of_n)-1))
            total_value += value_n

        return total_value


    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.BaseN_to_base10(s, self.alpha_value_dict)
