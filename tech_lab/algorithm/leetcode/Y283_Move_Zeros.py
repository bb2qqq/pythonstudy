# coding: utf-8
"""

Link: https://leetcode.com/problems/move-zeroes/


Description:
    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

    Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

"""
# 有两个思路，第一个思路是找出列表里有多少个0，把他们删除后，再将相同数目的0 extend到末尾

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_nums = nums.count(0)
        for i in range(zero_nums):
            nums.remove(0)
        nums.extend([0]*zero_nums)
