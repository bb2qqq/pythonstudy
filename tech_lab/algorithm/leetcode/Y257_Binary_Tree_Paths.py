# coding: utf-8

"""

Link: https://leetcode.com/problems/binary-tree-paths/

Description:

    Given a binary tree, return all root-to-leaf paths.

    For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
    All root-to-leaf paths are:

    ["1->2->5", "1->3"]

"""

# 看到此题，脑海里的原始想法是，从root开始走，遇到死路就回来，记录当时的路，回到上一级节点继续探索。如果全是死路就继续返回。
# 但是问题的难点是找出一个高效的方法记忆哪些路走过了，哪些路是新加入的。即不重复寻路。貌似这题很经典。
# 让我们从一个经典的三层完美二叉树开始:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# 我们先从1出发，到了2，发现左右都有路，我们走到左边的4，发现没路了，回去，好，继续走5，没路了，回去。
# OK！到了这一步，我们的算法必须理解，我们不能继续走4了。已经走过了。我们必须返回上一级了。
# 我想到的一个比较初级的方法是，左leaf无路可走的时候返回路径，同时返回上一级。
# 同时尝试右leaf, 右leaf无路可走的时候，向上返回两级。
# 但是，向上返回两阶段的时候，如何知道当前节点是左叶片还是右叶片呢？
# 在每一级的时候，我们能知道左叶片是什么，右叶片是什么。那么我们也能知道一个叶片是它上一级节点的左叶或者右叶。
# 那么如果一个叶片向上两级发现该节点是左叶，那么调用左叶逻辑，继续探寻右叶。如果是右叶，则再返回两级。
# 如果右叶片返回上去的节点是根节点。那么整个探索结束。
# 按照题设，貌似根节点的val是1。
# 这是一种解决问题的方法，或许还有其他更优的方法
#                                                                                       2015-09-01 13:08


# 只有left 或者 right 都是None, 才需要记录path
# 忽然发现貌似并不要对左右区分，往回跳两级之类的，循环遍历就好了
# 现在剩下的就是循环遍历如何表达了。
# 而且，照这个想法的话，原来的第一个思路完全可以精简。我把第一个思路实现后，要试试更简便的解法。
# 通过了。但是leetcode坑了我一把，说了传TreeNode实例进来，还给我来个None.
#                                                                       2015-09-01 17:41


# 开始考虑代码看起来更简洁的解决方法。其实另一种方法只不过是把路径放在每一个实例身上传递。
# 如果触底就返回身上的路径。
# 啊， 犯懒了，先搁这儿。休息，休息一会儿
#                                                                       2015-09-01 18:30

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None          # 我猜想此处是数字 # 然后我又觉得此处应该是个实例才对，必须是实例。
#         self.right = None

class Solution(object):
    """
    209 / 209 test cases passed.
    Status: Accepted
    Runtime: 52 ms
    Submitted: 0 minutes ago

    """

    def log_path(self, node):
        path = []
        while node.upper_node:
            path.append(node.val)
            node = node.upper_node
        path.append(node.val)       # The last node has no upper_node, but its value should be include in path
        path.reverse()

        formatted_path = "->".join(map(str, path))
        self.all_paths.append(formatted_path)

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

        return self.all_paths


class Solution_2(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """



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
