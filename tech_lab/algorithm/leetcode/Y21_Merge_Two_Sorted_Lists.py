# coding: utf-8
"""

Link: https://leetcode.com/problems/merge-two-sorted-lists/


Description:

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 最开始我以为只是要把两个list拼接在一起，后来通过提交答案的错误提示才明白，
# 两个列表拼接后，里面的节点数值也应当是有序的。
# 现在的想法是写一个val和节点的映射表，最后再把节点从大到小拼接起来

class Solution(object):
    """
    208 / 208 test cases passed.
    Status: Accepted
    Runtime: 68 ms
    Submitted: 3 minutes ago
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.agent_dict = {}
        self.upload_nodes(l1)
        self.upload_nodes(l2)
        merged_list = self.merge_current_nodes()
        return merged_list

    def merge_current_nodes(self):
        L = []
        for val in sorted(self.agent_dict.keys()):
            L.extend(self.agent_dict[val])
        for index, node in enumerate(L):
            if index == len(L) - 1:
                node.next = None
                break
            node.next = L[index + 1]
        if L:
            return L[0]


    def upload_nodes(self, list_node):
        """ 使用此方法时，list_node应当是个single_linked list"""
        while 1 and list_node:
            node_val = list_node.val
            if node_val in self.agent_dict:
                self.agent_dict[node_val].append(list_node)
            else:
                self.agent_dict[node_val] = [list_node]
            list_node = list_node.next
