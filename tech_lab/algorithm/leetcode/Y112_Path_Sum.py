# coding: utf-8
"""

Link: https://leetcode.com/problems/path-sum/


Description:

    Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

    For example:
    Given the below binary tree and sum = 22,

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    114 / 114 test cases passed.
    Status: Accepted
    Runtime: 104 ms
    """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if type(sum) != int:
            return False
        if not root:        # leetcode may pass None type in here shamelessly.
            return False

        self.has_target_sum = False
        self.sum_ = sum
        root.upper_node = None

        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)

        return self.has_target_sum

    def log_path(self, node):
        path = []
        while node.upper_node:
            path.append(node.val)
            node = node.upper_node
        path.append(node.val)     # The last node has no upper_node, but its value should be include in path
        if sum(path) == self.sum_:
            self.has_target_sum = True
        path.reverse()

        formatted_path = "->".join(map(str, path))


    def process_leaves(self, node):
        left_leaf = node.left
        right_leaf = node.right

        # Only assign upper_node when leaf is not None
        if left_leaf:
            left_leaf.upper_node = node
        if right_leaf:
            right_leaf.upper_node = node

        if not left_leaf and not right_leaf:
            self.log_path(node)  # Find a path, calculates its sum.

        if self.has_target_sum:  # There is a path whose sum equals to target.
            return False         # No need to continue traverse.
        else:
            return left_leaf, right_leaf

    def traverse_analyze(self, process_results):
        if not process_results:
            return
        for leaf in process_results:
            if leaf:
                process_results = self.process_leaves(leaf)
                self.traverse_analyze(process_results)
