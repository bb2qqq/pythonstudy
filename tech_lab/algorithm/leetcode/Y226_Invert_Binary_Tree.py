# coding: utf-8
"""

Link: https://leetcode.com/problems/invert-binary-tree/


Description:
    Invert a binary tree.

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    to
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

"""
# 看起来invert是让我们把每个叶片的左右翻转
# 那么我们首先需要找到所有的节点。然后再以一个不会导致错误的顺序，将各个节点依次翻转。
# 一种想法是先找到所有的节点，然后给这些节点分层级，先将最低层级的节点翻转，再翻转次一级节点，最后翻转root节点
#                                                               2015-09-15 20:48

# 有没有不找出所有节点就进行翻转的方法呢？我想有！
# 是的，通过了，但是比方法一用时更久。这说明leetcode的代码运行时间实际上和他们的服务器状态有关！
#                                                               2015-09-15 21:01

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    68 / 68 test cases passed.
    Status: Accepted
    Runtime: 80 ms
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:        # leetcode will pass None type in shamelessly here.
            return []
        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)
        return root

    def process_leaves(self, node):
        agent = node.left
        node.left = node.right
        node.right = agent
        return node.left, node.right

    def traverse_analyze(self, process_results):
        for leaf in process_results:
            if leaf:
                process_results = self.process_leaves(leaf)
                self.traverse_analyze(process_results)


class SolutionAccepted_1(object):
    """
    68 / 68 test cases passed.
    Status: Accepted
    Runtime: 44 ms
    """
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.all_paths = []
        if not root:        # leetcode will pass None type in shamelessly here.
            return []

        root.upper_node = None

        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)

        node_level_dict = {}

        for path in self.all_paths:
            for level, node in enumerate(path):
                if level in node_level_dict:
                    node_level_dict[level].update([node])
                else:
                    node_level_dict[level] = set([node])

        node_levels = node_level_dict.keys()
        node_levels.reverse()  # so it starts from the lowest level

        for node_level in node_levels:
            target_level_nodes = node_level_dict[node_level]
            for node in target_level_nodes:
                agent = node.left
                node.left = node.right
                node.right = agent
        return root

    def log_path(self, node):
        path = []
        while node.upper_node:
            path.append(node)
            node = node.upper_node
        path.append(node)       # The last node has no upper_node, but its value should be include in path
        path.reverse()

        self.all_paths.append(path)

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

