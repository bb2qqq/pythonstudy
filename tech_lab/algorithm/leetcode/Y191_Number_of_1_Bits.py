# coding: utf-8
"""

Link: https://leetcode.com/problems/number-of-1-bits/


Description:
    Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

    For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

"""

# 一个最简单的方式，先将整数转换成二进制，然后数里面有多少个1就好了
#                                                   2015-09-18 17:49

# 如果不做这一步，实际上就是做一个二进制转换了
# 先放在这儿。列为TODO， 以后有兴致的话做一个n进制的转换工具。
#                                                   2015-09-18 17:51

class Solution(object):
    """
    600 / 600 test cases passed.
    Status: Accepted
    Runtime: 44 ms
    Submitted: 0 minutes ago
    """
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_str_n = bin(n)
        hamming_weight = binary_str_n.count('1')
        return hamming_weight
