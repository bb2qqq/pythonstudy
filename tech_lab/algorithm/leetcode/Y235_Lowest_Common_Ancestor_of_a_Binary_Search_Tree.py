# coding: utf-8
"""

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


Description:

    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

            _______6______
           /              \
        ___2__          ___8__
       /      \        /      \
       0      _4       7       9
             /  \
             3   5
    For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

"""

# 要理解此题，必须先弄明白什么是lowest-common-ancestor。
# wikipedia链接：https://en.wikipedia.org/wiki/Lowest_common_ancestor
# 大概明白题目了，在lowestCommonAncestor一题里，自己也算自己的后代

# 首先我们得找到root到这两个节点的路径。按照二叉树的规则，如果两个节点到root的路径在中途没有交汇。
# 那么他们的共同祖先就是root节点
# 如果有交汇，那个交汇节点就是LCA
# 现在需要的是记录路径，其实也容易，把root节点一路上经过的节点放进list里。
# 到时候比较所有common 节点，选个index值最高的就好了

# 我去看自己之前另一题的答案了: Y257_Binary_Tree_Paths.py。
# 好，只要改一改log_path就好了
# 然后记录条件从达到尾部节点改成只要经过目标节点就记录
# 然后增加一个机制防止每次通过目标节点的时候都记录。
# 然后整个找路径在找到全部两条目标路径后应该停止
#                                                                       2015-09-09 17:14

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """

    27 / 27 test cases passed.
    Status: Accepted
    Runtime: 176 ms
    Submitted: 0 minutes ago

    """

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

        if node in self.target_nodes:
            self.log_path(node)
            self.target_nodes.remove(node)

        return left_leaf, right_leaf

    def traverse_analyze(self, process_results):
        if len(self.all_paths) == self.target_numbers:  # 找到所有目标path后退出
            return
        for leaf in process_results:
            if not leaf:
                continue
            process_results = self.process_leaves(leaf)
            self.traverse_analyze(process_results)


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.all_paths = []
        self.target_nodes = [p, q]  # 只在最终path包含这两个节点的时候记录path
        self.target_numbers = len(self.target_nodes)
        if not root:        # leetcode will pass None type in shamelessly here.
            return []

        root.upper_node = None

        # self.all_path will be filled with target_path in this process
        process_results = self.process_leaves(root)
        self.traverse_analyze(process_results)

        path_1, path_2 = self.all_paths
        longer_path = max(path_1, path_2)
        common_nodes = set(path_1) & set(path_2)

        # 没有LCA的话，return None
        if not common_nodes:
            return

        LCA = max(common_nodes, key=longer_path.index)
        return LCA

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
