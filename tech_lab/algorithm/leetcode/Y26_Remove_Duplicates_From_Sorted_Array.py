# coding: utf-8
"""

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


Description:
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place with constant memory.

    For example,
    Given input array nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

"""

# 哈哈，我简直草你妈了，python不能在for循环的时候删除元素，不让我用额外内存，我搞你麻痹啊，哈哈。
# 不管了我就是要新内存。
# 唉哟我操，貌似还真有一种思路，那就是先将重复的元素扔到最后面去，计算重复元素的个数，最后将列表后几位值删掉。
# 我好饿！

# 妈的，我要自己改题目要求了，可以用额外的内存，但是时间复杂度要小于n*n，最好是n的时间复杂度。
# 题目说了这是个sorted array......忘了这条件了，在discuss里找到了一个pythonic的回答。。

class Solution(object):
    """

    161 / 161 test cases passed.
    Status: Accepted
    Runtime: 196 ms
    Submitted: 0 minutes ago

    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = [nums[i] for i in range(len(nums)) if (i==0 or nums[i-1] != nums[i])]   # 根据Discuss里他人的方案，两日后回忆而作
        return len(nums)
