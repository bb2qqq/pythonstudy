# coding: utf-8
"""

Link: https://leetcode.com/problems/valid-anagram/


Description:

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

"""

# 看到这个题目，首先肯定要搞明白anagram的意思啦，去OALD上查了下:
# a word or phrase that is made by arranging the letters of another word or phrase in a different order
# Example: An anagram of ‘Elvis’ is ‘lives’.
# 所以anagram还存在一个大小写判断的问题？先不考虑这个
# 嗷，发现题设里说了只有lowercase
# 那么在python里，只要返回sorted(a) == sorted(b)就好了啊。
# 当然，我们可以考虑一种不使用内置sorted函数的解法。。
#                                                               2015-09-02 22:01

# 我们来试试第二种方法。


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution_2(object):

    def count_chars(self, target_str):
        D = {}
        for i in target_str:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        return D

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = self.count_chars(s)
        count_t = self.count_chars(t)

        return count_s == count_t
