# coding: utf-8
"""

Link: https://leetcode.com/problems/reverse-linked-list/


Description:
    Reverse a singly linked list.

    Hint:
    A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先来一个iterative的方法吧
# 需要考虑最后next是None时的临界状况

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        previous_node = None
        while True:
            next_node = head.next
            if previous_node:
                head.next = previous_node
            if not next_node:
                break
            previous_node = head
            head = next_node

        return head
