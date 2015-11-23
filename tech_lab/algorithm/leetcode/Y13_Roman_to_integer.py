# coding: utf-8
"""

Link: https://leetcode.com/problems/roman-to-integer/


Description:
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

"""

# 想做这道题，首先得了解罗马数字标记的规则。
# 除了罗马数字到10进制数字的转换。我还要做一个10进制数字到罗马数字的逆转换！
#                                                          2015-09-06 21:26
#
# 上wikipedia看了下罗马数字的介绍：https://en.wikipedia.org/wiki/Roman_numerals
# 对应表： I-1 V-5 X-10 L-50 C-100 D-500 M-1000
# 一般情况下，字符从大到小由左到右依次排开
# 如果小的排在大的前面，减法被应用。
# I，X，C三个数字可以用作减法元素，置于比他们高一级或两级的元素前

# 注：为了表示10000以上的数字，有一种貌似不是官方的作法，就是把除去I以外的数值头上加一横，表示乘以1000倍

# 麻烦的地方，就在于处理减法。
# 回家路上慢慢想！
#                                                              2015-09-06 21:56

# 貌似现代减法只允许一个元素相减。这样貌似还是容易些
# 那么一个字符只需与它后面的字符相比较就OK, 同级或者高级，则相加。低级则相减。
# 不过想到一个反例，我如何处理XIV? 照上面的逻辑，加起来就是16，which is wrong.
# 回家路上想想吧！这次是真的。
#                                                              2015-09-06 22:00

# 昨晚上在路上想了一下，一个字符后面跟的字符只有两种情况，排序高于该字符，或不高于该字符。

# 当出现第一种情况时，用后一个字符的值减去当前值。当出现第二种情况的时候。（思绪在此处变更）
# 首先我们想象一个指针，指针指向第一个字符，我们的value_pool里的值是当前字符代表的值。
# 如果起始值后面跟着的是比它高的值，用后一个值减去起始值，指针移到
# 接着该值后面出现一个比该值低的值，
# 思绪乱掉了。

# 我观察到。表示减法的数值只有一种情况，就是“小大”，即只有4，9，40，90，400，900是用减法表示的。
# 所以一个字符组可能是一个单字符，或者一个“小大”组合。
# 字符组是按最大的在左边，依次向右递减排列。
# 实际上，在计算时，我们不用管顺序，只要把每个字符组加起来就好了。
# 只需写一个决定字符组的逻辑就好了！
#                                                               2015-09-07 12:25

# 开始写十进制数字转换到罗马的工具（/Users/zen1/zen/pythonstudy/tech_lab/utils/python_scripts/Roman_decimal_converter.py)


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_char_rank = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        index = 0
        total_value = 0
        while index < len(s):
            current_char = s[index]
            current_char_value = roman_int_map[current_char]

            if index + 1 == len(s):     # 指针移到最后一个字符
                total_value += current_char_value
                break

            next_char = s[index + 1]
            next_char_value = roman_int_map[next_char]

            if roman_char_rank.index(current_char) >= roman_char_rank.index(next_char):
                total_value += current_char_value
                index += 1
            else:
                total_value += ( next_char_value - current_char_value)
                index += 2

        return total_value


    def int_to_roman(self, number, allow_minus=True):
        """ 输入int, 返回对应的罗马字符。
            默认开启减法表达，allow_minus=False关闭减法表达。该功能尚未完成（TODO)
            只支持1万以内的数字转换。
        """
        int_roman_map = {1: ('I', 'V', 'X'), 10: ('X', 'L', 'C'), 100: ('C', 'D', 'M'), 1000: ('M', '?', '?')}

        if not type(number) == int or not 1 <= number <= 9999:
            print "只支持1至9999间的整数转换。"
            return

        # 将1905转成[1000, 900, 0, 5]这样的列表
        expression = str(number)
        expr_length = len(expression)
        base = 10
        value_list = []

        for index, digit in enumerate(expression):
            digit_rank = abs(index - expr_length)
            digit_value = int(digit) * (base**(digit_rank-1))
            value_list.append(digit_value)

        # 将形式如同[1000, 900, 0, 5]的列表转成罗马数字
        roman_expression = ''
        for decimal_value in value_list:
            first_digit = int(str(decimal_value)[0])
            # 罗马数字里没有0的表示
            if first_digit == 0:
                continue

            digit_numbers = decimal_value/first_digit
            unit_1_char, unit_5_char, unit_10_char = int_roman_map[digit_numbers]
            if digit_numbers == 1000:
                agent_expr = unit_1_char * first_digit
            else:
                if first_digit == 4:
                    agent_expr = unit_1_char + unit_5_char
                elif first_digit == 9:
                    agent_expr = unit_1_char + unit_10_char
                elif first_digit < 5:
                    agent_expr = unit_1_char * first_digit
                else:
                    first_digit -= 5
                    agent_expr = unit_5_char + unit_1_char * first_digit

            roman_expression += agent_expr

        return roman_expression
