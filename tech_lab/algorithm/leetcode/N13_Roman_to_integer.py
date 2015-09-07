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

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
