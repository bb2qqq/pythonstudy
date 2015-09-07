# coding: utf-8
"""

Link: https://leetcode.com/problems/ugly-number/


Description:
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

"""

# 要解出这道题，我们需要找到一个方法，来找出一个数的所有factor, 然后判断里面除了2, 3, 5外有没有其他元素
# 一种反向思维的方式是，拿目标数与2, 3, 5循环相除，看最终的结果里是否有除三个ugly factor 外的其他factor
# 如果一个正整数和2，3，5都不能相除，那么它必定是一个ugly number
#                                                                                       2015-08-28 11:17

# 忽然想起一事，is_dividable函数需要加入 1 这个边界条件, 不然就会陷入无限循环。因为1可以一直被自己除。
# 而且，我需要去wikipedia了解一下prime factor的概念。

# Link: https://en.wikipedia.org/wiki/Prime_factor
# The prime factor of a positive integer are the prime numbers that divide that interger exactly.
# The prime factorization of a positive integer is a list of the interger's prime factors, together with their multiplicities.
# Example: 360 = 2 x 2 x 2 x 3 x 3 x 5

# 也就是说，一个正整数的prime factors是那些相乘起来等于该正整数的质数的列表。
#                                                                                       2015-08-28 12:35

# 我想我应该拿这个正整数与2, 3, 5依次相除，看是否有成功的。
# 如成功相除，所得的因子再与2，3，5尝试相除，直到最后的结果是1或某个不能与2，3，5相除的数为止

# 在leetcode上提交的前两次都失败了，第一次是因为leetcode不支持import
# 第二次是因为没有判断输入值不是正整数的情况！
#                                                                                       2015-08-28 16:56




# 因为leetcode不支持import, 所以将此行引用删掉
# from __future__ import division

class Solution(object):

    def attempt(self, numerator, denominator):

        float_result = float(numerator)/denominator
        int_result = int(float_result)
        if float_result == 1:
            return False, int_result
        elif float_result == int_result:
            return True, int_result
        else:
            return False, numerator

    def ugly_divide(self, num):
        for factor in [2, 3, 5]:
            sig, divide_result = self.attempt(num, factor)
            if sig:
                divide_result = self.ugly_divide(divide_result)
                break

        return divide_result

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if type(num) != int or num <= 0:
            return False

        ugly_set = set([1, 2, 3, 5])

        result = self.ugly_divide(num)

        if result not in ugly_set:
            return False
        else:
            return True
