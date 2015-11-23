# coding: utf-8
"""

Link: https://leetcode.com/problems/plus-one/


Description:
    Given a non-negative number represented as an array of digits, plus one to the number.

    The digits are stored such that the most significant digit is at the head of the list.

"""
# 用python做这道题，简直是作弊

class Solution(object):
    """
    Accepted
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        origin_str = ''.join(map(str, digits))
        decimal_num = int(origin_str)
        decimal_num += 1
        increased_str = str(decimal_num)
        increased_array = [int(i) for i in increased_str]
        return increased_array


class SolutionFailed1(object):
    """
        Input:
        [9]
        Output:
        [10]
        Expected:
        [1,0]

    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        return digits
