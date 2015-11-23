# coding: utf-8
"""

Link: https://leetcode.com/problems/house-robber/


Description:
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""

# 如果用X表示已抢劫，O表示未抢劫，那么 XXX 和 XOX 都是禁止出现的pattern
# 从逻辑上而言，应当先抢劫高价值的。
# 但这规则可能会失效，让我们以 587908 为例，我们抢了中间的9, 两边的8都不能抢了。。实际上我们得到的总价值是9，而非最优的18

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        disable_set = set([])
        agent_list = []
        for index, val in nums:
            agent_list.append((val, index))
        while len(disable_set) != len(nums):
            max_tuple = max(set(agent_list) - disable_set)
            disable_set.update([max_tuple])

        for index, val in enumerate(nums):
