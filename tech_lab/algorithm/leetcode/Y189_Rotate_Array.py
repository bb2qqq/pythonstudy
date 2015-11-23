# coding: utf-8
"""

Link: https://leetcode.com/problems/rotate-array/


Description:

    Rotate an array of n elements to the right by k steps.

    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

    Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

"""
# 要求三种解题方法，心也太大了吧。
# 先来一种！
# 此题不准return，让直接改列表对象。
# 一种比较取巧（也许是唯一办法）是建一个临时列表储存结果，再把原始列表里的值改成和临时列表相同
# 向右移实际上是序号增加，序号超过列表长度-1后，从0开始计算。用增加后序号余列表长度 = 当前序号
# 好了，第一个方案Accepted了。
#                                                                       2015-09-11 11:24

# 第二个设想是，先将k的值与列表长度相余得到真实需要位移的步数。
# 接着将依据步数生成两个切割后列表。将两个切割列表交换次序拼接后得到转换后列表。
# 然后将原列表里的值改成转换后列表的值。
# real_k值可能是正，可能是负，
# 看了下余数的概念，对于给定的两个自然数a，b，如果b不等于0，那么一定存在两个自然数q和r
# 使得 q*b + r = a， 且0 <= r < b
# 以-5 % 4 为列，得到的坐标是3。而我预想的是-1
# 但是转念一想，-1 和 3 在长度为4的列表里，指代的位置是一样的。
# 所以我们现在的取模方法对正负数都是有效的
# 第二个方案成功了
#                                                                       2015-09-11 15:26

# 那么第三种方法是什么呢？我们可以一个个的取值，先找到real_k。
# 如果要发生替换的话，被替换的值一定会去替换其他的值
# 所以我们可以使用一个临时变量，在进行替换的时候储存被替换的值，
# 然后用找到被替换的值现在应该放在哪，继续替换，直到循环达到列表长度
# 这种思路有缺陷比如，rotate([1,2,3,4], 2), 1会替换3的位置，而3会替换1的位置。
# 然后就没2和4的替换了。
# 所以硬要找3个solution的话，先生成一个空列表。然后将依次赋值，最后再赋回来


class SolutionAccepted_3(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        33 / 33 test cases passed.
        Status: Accepted
        Runtime: 88 ms
        """
        list_length = len(nums)
        L = [0] * list_length
        for index, value in enumerate(nums):
            altered_index = (index + k) % list_length
            L[altered_index] = value

        for index, value in enumerate(L):
            nums[index] = value


class SolutionAccepted_2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        33 / 33 test cases passed.
        Status: Accepted
        Runtime: 124 ms
        """
        real_k = k % len(nums)
        if real_k:  # real_k为0不需改变
            slice_piece = nums[-real_k : ]
            rest_piece = nums[ : -real_k]
            rotated_list = slice_piece + rest_piece

            for index, value in enumerate(rotated_list):
                nums[index] = value


class SolutionAccepted_1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.

        33 / 33 test cases passed.
        Status: Accepted
        Runtime: 88 ms
        """
        D = {}
        list_length = len(nums)
        for index, value in enumerate(nums):
            altered_index = (index + k) % list_length
            D[altered_index] = value

        for index, value in D.items():
            nums[index] = value
