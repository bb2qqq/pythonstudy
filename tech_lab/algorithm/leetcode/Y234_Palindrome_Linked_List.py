# coding: utf-8
"""

Link: https://leetcode.com/problems/palindrome-linked-list/


Description:

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

"""

# 首先，我得理解 palindrome 是什么
# https://en.wikipedia.org/wiki/Palindrome
# 理解了，palindrome就是正着读反着读，字母序一样的单词，比如Dad，妈妈，叨逼叨
# 那么先做一个可用的solution再考虑follow up里的进阶要求吧

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#                               2015-09-10 13:07

# 开始做常数量的空间使用的实现了
# 我拿自己的脑子想了一下， 唉哟，好难，甚至，在心里说，这用python根本就做不出来嘛。不做了。
# 之后，我抱着好奇的心态，上Discuss区看了下别人的回答。竟然找到一个牛逼且简洁的算法，并且可以实现空间上的O(1)。
# https://leetcode.com/discuss/46304/python-understand-solution-comments-operate-nodes-directly
# 折服了。开眼界了。
# 算是勉强看懂了作者的实现，自己来做一遍！

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        # 找到列表的中点
        # 在列表长度为奇数情况下，最终状态slow是中间的节点，fast是结尾的节点。
        # 在列表长度为偶数情况下，最终状况slow是(列表长度/2) + 1的节点，fast是None。
        while fast and fast.next:
            fast = fast.next.next  # fast一次走两步。
            slow = slow.next       # slow一次走一步。
        current_node = mid_node = slow

        # 奇数长度列表的中间节点的值不会影响列表是palindrome与否。
        # 所以我们只需要以第一步得到的中点作为起点，从列表末尾的节点，将next指向反转依次向前指回中点。
        # 再将最后一个节点和第一个节点放一起，并排比较val，如果相同就比较他们的下一个节点值是否相同，一直到最后一对。
        # 但是如何判断最后一对呢？
        # 有一种考虑方法，是将中点的next值设为None. 然后判断比较节点中任意一个的下一节点是None的话，比较循环终止。

        # 那么反转指向如何做呢，我们先要找到某个节点的下一个节点，将该节点指回原节点。
        # 同时在指回前，我们需要先要想办法获得下下一个节点。否则逻辑链条就断了！

        # 这样中点的next标签往回指的时候，赋值得到None，为第3步的终止比较做准备
        previous_node = None
        while current_node:                    # 当前节点不为空则一直循环
            next_node = current_node.next      # 将next_node的标签变量指向current_node标签变量所指示的对象的的next节点对象
            current_node.next = previous_node  # 当前节点对象的next标签变量反向指回previous_node标签变量所指代的对象，即上一个节点对象
            previous_node = current_node       # 将previous_node标签变量指向current_node标签变量所指示的节点对象
            current_node = next_node           # 将current_node的标签变量指向当前节点的next节点对象

        # 上一步while循环终止时，current_node是None了，实际的current_node存放在previous_node变量里
        while previous_node:
            if previous_node.val != head.val:
                return False
            previous_node = previous_node.next
            head = head.next
        return True   # 没有出现False的情况下，说明是palindrome, 返回True

class SolutionAccepted_1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        21 / 21 test cases passed.
        Status: Accepted
        Runtime: 200 ms
        Submitted: 0 minutes ago

        But this isn't O(1) in space.
        """
        L = []
        current_node = head
        while True:
            if not current_node:
                break
            L.append(current_node.val)
            current_node = current_node.next

        origin_str = ''.join(map(str, L))
        L.reverse()
        reversed_str = ''.join(map(str, L))

        return origin_str == reversed_str


class SolutionFailed_1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        Submission Result: Wrong Answer More Details

        Input:
        [1,0,0]
        Output:
        true
        Expected:
        false

        错误原因，sorted不是reverse!

        """
        L = []
        current_node = head
        while True:
            if not current_node:
                break
            L.append(current_node.val)
            current_node = current_node.next

        return L == sorted(L, reverse=1)
