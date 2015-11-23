# coding: utf-8
"""

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/


Description:
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# 看到这道题，我感觉又要借用之前的原型了。。。
# 只要把原来的log path改成log长度就OK了。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    38 / 38 test cases passed.
    Status: Accepted
    Runtime: 92 ms
    Submitted: 0 minutes ago
    """
    def log_path(self, node):
        path = []
        while node.upper_node:
            path.append(node.val)
            node = node.upper_node
        path.append(node.val)       # The last node has no upper_node, but its value should be include in path

        self.all_paths.append(len(path))

    def process_leaves(self, node):
        left_leaf = node.left
        right_leaf = node.right

        if left_leaf:
            left_leaf.upper_node = node

        if right_leaf:
            right_leaf.upper_node = node

        if not left_leaf and not right_leaf:
            self.log_path(node)

        return left_leaf, right_leaf

    def traverse_analyze(self, process_results):
        for leaf in process_results:
            if leaf:
                process_results = self.process_leaves(leaf)
                self.traverse_analyze(process_results)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.all_paths = []
        if not root:        # leetcode will pass None type in shamelessly here.
            return 0

        root.upper_node = None

        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)

        return max(self.all_paths)




###   测试用例区域

class TreeNode(object):
    """ Made this Class for test """

    def __init__(self, x):
        self.val = x
        self.left = None          # 我猜想此处是数字 # 然后我又觉得此处应该是个实例才对，必须是实例。
        self.right = None


#  测试用节点说明：
#         1
#       /   \
#      2     3
#     / \     \
#    4   5     6
#   / \
#  7   8

n7 = TreeNode(7)
n8 = TreeNode(8)
n5 = TreeNode(5)
n6 = TreeNode(6)

n4 = TreeNode(4)
n4.left = n7
n4.right = n8

n3 = TreeNode(3)
n3.right = n6

n2 = TreeNode(2)
n2.left = n4
n2.right = n5

n1 = TreeNode(1)
n1.left = n2
n1.right = n3
