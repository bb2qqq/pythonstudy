# coding: utf-8
"""

Link: https://leetcode.com/problems/delete-node-in-a-linked-list/


Description:
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

"""
# 看了下这道题，大概的难点在于删除一个节点后，要将该节点的上一个节点的next的值改成该节点的next的值
# 我觉得一会儿洗了澡有必要看看什么是linked list
# 看了下Linked list的简介。发现此题的关键，是找到被删除的node的上一个对象。。不过貌似我是找不到的，题目没有告诉我！
# 我升起了一个想法，那就是伪删除。。。也就是说，让当前节点和它的下一节点表现的完全一样。。我们就可以认为该节点已经被正确删除了。
# 也就是说，张三要去找他的下家李四。现在李四根据基本法应当被删除。但是只有李四知道他的下家是谁。删了李四击鼓传花就没法儿玩了。
# 然后李四说：好的，我变，李四把他下家王五找过来。把自己变成王五的一个克隆体。。
# 这样，张三找的是变成王五的李四。由李四变成的王五知道王五的下家是谁。击鼓传花继续。只有可怜的真の王五被孤零零的晾在一旁。组织已经不需要他了。
#                                                                                                                       2015-09-03 22:26

# Solution 通过了。我在想，如果我把1到100间除了1和100外所有的节点都用这个solution删掉。实际上发生了什么呢？
# 首先我们删掉2号，2号变成了克隆3号。如果3号也需要被删除，会发生什么？
# 我们不能删除原来的3号。我们需要删除克隆的3号，因为1号并不知道真正的3号是谁。
# 所以把2,3,..,99这些节点删除，在这个python solution里，实际上是把二号节点的val和next值不断改变，直到改成val=100, next=None
# 而原来的2号到99号的节点们stay untouched. 从未被删除。
# 或许这是python 的语言特性导致的。只能出现这样一个模拟的solution. 在其他底层语言里，解法可能更干脆一些
#                                                                                                                       2015-09-03 22:49


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        83 / 83 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        Submitted: 0 minutes ago
        """
        node.val = node.next.val
        node.next = node.next.next
