# coding: utf-8
"""

Link: https://leetcode.com/problemset/algorithms/


Description:
    Given an array and a value, remove all instances of that value in place and return the new length.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

"""

# 此题最有意思的是删除某个列表里值等于输入值的元素，而且不可以使用到copy，必须在原列表里操作。
# python在操作列表的时候，不能在for循环遍历删除。。。那也就是说用index删完后下一个index必须减1，因为列表长度变了，而且这个index列表必须是有序的。

class Solution(object):
    """
    112 / 112 test cases passed.
    Status: Accepted
    Runtime: 44 ms
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        agent_list = []
        for index, value in enumerate(nums):
            if value == val:
                agent_list.append(index)
        new_length = len(nums) - len(agent_list)

        # 删除原列表里的指定值
        mod_val = 0  # 删除值后列表长度会变化，需要用一个值来进行修正
        for index in agent_list:
            real_index = index + mod_val
            del nums[real_index]
            mod_val -= 1

        return new_length
