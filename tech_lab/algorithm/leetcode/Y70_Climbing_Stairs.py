# coding: utf-8
"""

Link: https://leetcode.com/problems/climbing-stairs/


Description:
    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

# 这道题可以抽象为一个连续列表，可按划分尺度列表[x, y, n, ...]里的长度进行任意连续切割，问有多少种可能结果
# 最理想的状况是写出这个通用规则后，把[1, 2]传入。
# 比较聪明的方法是写一个全覆盖且不重复搜索的遍历。
# 比较笨的方法是写一个全覆盖但会重复搜索的遍历，最后去重。

# 明白了，在面临第一种选择时，我们有若干个选择，我们依次尝试这若干个选择，在每个选择下面仍然有多个选择。
# 我们继续依次选择，像一个树一样从顶部分开。只要控制边界条件即可（所选元素不超出现有列表）

# 在写作的过程中，我是先写一个demo，然后根据结果进行改错。
#                                                                       2015-09-24 12:25

# 第一种想法失败了，虽然可以获得所有的组合，但是算法复杂度太高了。
# 或者，我们可以把整个列表看做是一个n个位置的队列
# 然后我们根据切割尺度，穷举所有可能的组合。
# 以每一个组合的长度作为该组合队列长度，组合里不为1的元素当做基数，求一个Permutation数。
# 将所有permutaion数相加，得出最终结果
#
# TODO
# n个元素按[x, y, z, ...]里的可选尺度进行任意切分的不相同方法，我们可以看做
# 用[x, y, z, ...]里的元素相加得到n，共有多少种不同加法，不考虑顺序
# 我们用一个不会重复的循环遍历这些加法，对加法里的元素个数求响应permutation数
# 将所有permutation数相加。
#                                                                   2015-09-25 15:30

# 9月25日思考的那个方案，很好，但是n个元素按[x, y, z]切分的问题，我还没找到解决方法，先简单粗暴解决按1，2切分的情况好了。
#                                                                   2015-09-29 17:43

# 我之前的想法有漏洞，在遍历了所有可能的不同slice组合后，实际上不是求Permutation，而是求另一个combanation. 我们可以把一个8长度的列表想象成一个队列，如果我们按, 1, 1, 2, 2, 2切分的话，实际上我们要做的是

class Solution(object):
    """
    45 / 45 test cases passed.
    Status: Accepted
    Runtime: 44 ms
    Submitted: 0 minutes ago
    """
    def climbStairs(self, n, step_list=[1,2]):
        """
        :type n: int
        :rtype: int
        """
        total_possibilities = 0
        # get permutation for all possible slice combinations
        for i in range(n/2 + 1):
            if 2*i > n:
                continue
            elements_num = n - 2*i + i  # n - 2*i 是元素1的个数，i是元素2的个数
            total_possibilities += self.get_combination(elements_num, i)
        return total_possibilities

    def get_permutation(self, n):
        agent_num = 1
        for i in range(1, n+1):
            agent_num *= i
        return agent_num

    def get_combination(self, n, k):
        return self.get_permutation(n)/(self.get_permutation(k)*self.get_permutation(n-k))


class SolutionFailed1(object):
    """ 目前此种方法failed了，超时, 在输入值为35的时候。此方法可以获得解，但算法复杂度太高。但是此种方法可以显示出所有的组合。
    """
    def climbStairs(self, n, step_list=[1,2]):
        """
        :type n: int
        :rtype: int
        """
        self.possible_steps = step_list
        self.all_combinations = []
        self.slice_with_multiple_scales(range(n), self.possible_steps)
        return len(self.all_combinations)

    def slice_with_multiple_scales(self, target, step_list, current_index=0, current_pieces=[]):
        """ 一个任意长度的有序列表，可以按照参数列表里提供的n种尺度进行连续切分，返回最后可能的切分结果总数"""
        target_length = len(target)
        for step in step_list:
            clone_pieces = current_pieces[:]   # doing a new copy
            slice_index = current_index + step
            piece = target[current_index : slice_index]
            clone_pieces.append(piece)
            if slice_index == target_length:
                self.all_combinations.append(clone_pieces)  # You can add a count here, too.
            if slice_index < target_length:
                # continue slicing
                self.slice_with_multiple_scales(target, step_list, slice_index, clone_pieces)
