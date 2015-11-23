# coding: utf-8
"""

Link: https://leetcode.com/problems/majority-element/


Description:
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Credits:
    Special thanks to @ts for adding this problem and creating all test cases.

"""
# 太简单了，无需写出想法。
#                                                           2015-09-18 18:27


class Solution(object):
    """ 此方法比起第一个失败的方案而言，只会count不重复的元素 
        42 / 42 test cases passed.
        Status: Accepted
        Runtime: 52 ms
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = set(nums)
        majority_element = max(S, key=nums.count)
        return majority_element


class SolutionFailed_1(object):
    """ 此方案会导致超时 """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = max(nums, key=nums.count)
        return majority_element
