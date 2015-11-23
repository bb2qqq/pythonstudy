# coding: utf-8
"""

Link: https://leetcode.com/problems/pascals-triangle/


Description:
Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    [1,5,10,10,5,1]
   [1,6,15,20,15,6,1]
    ]

"""

# 看了下Pascal's Triangle（杨辉三角）的介绍，总结出如下规律
# 第n排有n个元素
# 两个端点的元素是1
# 非端点元素，等于上一排占据该端点序号的值，加上上一排该端点序号减一位置处的值'

class Solution(object):

    """

    15 / 15 test cases passed.
    Status: Accepted
    Runtime: 176 ms
    Submitted: 0 minutes ago

    """

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        previous_row = []
        for row_index in range(numRows):
            agent = [0] * (row_index + 1)
            for num_index in range(row_index + 1):
                if num_index == 0 or num_index == row_index:
                    num_val = 1
                else:
                    num_val = previous_row[num_index] + previous_row[num_index-1]

                print row_index, num_index, agent
                agent[num_index] = num_val
            previous_row = agent
            result.append(agent)

        return result
