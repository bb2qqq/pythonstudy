# coding: utf-8
"""

Link: https://leetcode.com/problems/contains-duplicate/


Description:
    Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

"""

# 我去，太简单了。。。
# 只要比较该列表的集合长度和该列表是否相等就OK了。
#                                   2015-09-18 18:05

# 如果我不能使用set关键词呢？
# 那这样的话则必须要用到i in N这样一种

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums) != len(set(nums))
