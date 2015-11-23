# coding: utf-8
"""

Link: https://leetcode.com/problems/power-of-two/


Description:

    Given an integer, write a function to determine if it is a power of two.

"""
# 如果一个数是power of 2，除以2若干次后，得到的数是1。
# 所以我们只要把输入值在大于1的情况下，一直除2。
# 如果最后的结果等于1，就是2的倍数。最后的结果小于1，就不是2的倍数
# 需要考虑输入值为1的情况

# 嗷，忽然想起来，还有负整数，得加入绝对值比较

# 我擦，第一次提交时错了，忽然想起来1也是power of 2, 2的power0... Oh..

# 第二次提交也错了，忘记加浮点数了。。。，OMG

# 第三次提交还是错了。。。。。。。。原因在于我没理解对power of 2的概念
# -16并不是power of 2, 0.0625 才是2的power of-4
# 解题思路得换叻。。。

# 嗷，这题是求一个整数是否是2的power，那么我们能否扩展为任何实数是否是2的power呢？

class Solution(object):
    """
    1108 / 1108 test cases passed.
    Status: Accepted
    Runtime: 68 ms
    """
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        if n < 1:
            while n < 1:
                n *= 2.0
        else:
            while n > 1:
                n /= 2.0
        return n == 1

class SolutionFailed2(object):
    """ 当输入值为0的时候，会无限循环。 """

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            while n < 1:
                n *= 2.0
        else:
            while n > 1:
                n /= 2.0
        return n == 1


class SolutionFailed1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while abs(n) > 1:
            n /= 2.0
        return abs(n) == 1
