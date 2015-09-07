# coding: utf-8

"""
Original link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Description:

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

# 一个最暴力的想法是，直接把两个列表拼接在一起，使用sorted来排序, 但是sorted算法，本身具有 n*log(n)的复杂度，不符合题设要求。           2015-08-27 11:09

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
