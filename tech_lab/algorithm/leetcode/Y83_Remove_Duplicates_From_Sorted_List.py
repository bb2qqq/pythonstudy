# coding: utf-8
"""

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/


Description:
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    For example,
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.

"""

# 一个想法是，拿一个set记录所有已知的val, 如果出现duplicate，就把前一个Node的节点直接指向到本节点的下一节点


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    164 / 164 test cases passed.
    Status: Accepted
    Runtime: 68 ms
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        val_pool = set([])
        node_list = []

        while True:
            if head.val not in val_pool:
                node_list.append(head)
            val_pool.update([head.val])

            head = head.next
            if not head:
                break

        for index, node in enumerate(node_list):
            if index + 1 < len(node_list):
                node.next = node_list[index+1]
        node_list[-1].next = None

        return node_list[0]


class SolutionFalied_1(object):
    """ 此方案在输入[1,1,1]后，会返回[1,1], 没有考虑到最后一个节点重复的情况。
        不对，这种方案不止没考虑到最后一个节点，它整个的next指向是跳着走的。。。
        我还不如直接建个列表。把所有值不重复的节点放进去，最后把里面一个个连起来就好
        最后一个节点的next指向None
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        val_pool = set([])

        origin_node = previous_node = head

        while True:
            next_node = head.next
            if head.val in val_pool:
                previous_node.next = next_node

            val_pool.update([head.val])
            previous_node = head
            head = next_node

            if not head:
                break

        return origin_node


# TEST AREA
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(1)
n5 = ListNode(1)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
