# coding: utf-8
"""

Link: https://leetcode.com/problems/same-tree/


Description:
    Given two binary trees, write a function to check if they are equal or not.

    Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

# 先把之前的Binary Tree全路径代码复制过来。
# 这回复习下怎么找全路径的。
# 该全路径发掘思路是这样的：
# 1. 给每个节点增加一个upper_node属性，root的upper_node是None，其他节点upper_node都不为None.
# 2. 遍历根节点的left和right叶片，将他们的upper_node设为root节点。
# 3. 同时查看left和right叶片的子叶片是否都为None，并将其upper_node标为对应的上一级节点。
#    如果都为None，返回上一级继续遍历。如不为None，继续循环遍历。
# 4. 循环遍历完毕，返回全路径

# 所以，我们此处，只需要比较两个节点的全路径的集合是否相等就OK了
# 注意，对[[1,2], [2,3]]进行set()操作会报错，必须把子列表转换成元组才可以进行set操作
# 第一次运行的时候报错了。错误信息是
#
# Input:
# [1,2], [1,null,2]
# Output:
# true
# Expected:
# false
#
# 并没有想明白自己哪儿错了，去leetcode上提问了。


class Solution(object):
    """
    209 / 209 test cases passed.
    Status: Accepted
    Runtime: 52 ms
    Submitted: 0 minutes ago

    """

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.binaryTreePaths(p) == self.binaryTreePaths(q)

    def log_path(self, node):
        path = []
        while node.upper_node:
            path.append(node.val)
            node = node.upper_node
        path.append(node.val)       # The last node has no upper_node, but its value should be include in path

        self.all_paths.append(tuple(path))

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

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.all_paths = []
        if not root:        # leetcode will pass None type in shamelessly here.
            return []

        root.upper_node = None

        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)

        return set(self.all_paths)


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
