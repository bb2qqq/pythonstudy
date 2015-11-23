# coding: utf-8
"""

Link: https://leetcode.com/problems/zigzag-conversion/


Description:
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

# 此题的难点在于如何理解第二个参数，numRows。
# 大概明白了。奇数行字符之间有一个空格，偶数行没有空格。这样每一行的字符数(包含空格)必然是奇数。
# 在排成n行的同时最后一行的字符数尽可能的和前一行的字符数接近。

# 等等，貌似我，题目没有理解对
# 字符顺着往下扑，达到指定的row数后，就起一个新的column。
# 按第一个row是第 0 row, 第一个column是第 0 cloumn算， 偶数column全填满，奇数column的偶数列是空的。
# 我甚至不用去生成题列里的形状。
# 哦，最后的需求是将横排之间的字符连起来。
# 那么需要给每个节点一个key, 然后一个value, 到时候按key取就好。
# 更方便的情况，是给每一个row一个列表，然后往列表里塞字符。最后把列表join起来就好
# 列表可以通过序号: 值的形式放在一个字典里，方便自动化
#                                                                   2015-09-07 18:27

#    167 / 1158 test cases passed.
#    Status: Wrong Answer
#    Submitted: 4 minutes ago
#    Input:
#    "ABC", 2
#    Output:
#    "ABC"
#    Expected:
#    "ACB"
#
# 第一次提交失败了，感情这个zig-zag规则不同的row数还不一样嘛，好嘛。。
# 之前的zigzag规则猜想失败了
# ABC, 2 的输出应该是:
#   AC
#   B
#
# 又错了。。
# 丢
#                                                                   2015-09-07 21:27


# 昨天看了一下别人的解答。。终于明白zigzag是什么样了。。在这儿作者想表达的形状是N型。如
# M     S     H     U
# A   E U   C A   G A
# R O   N U   C O   P
# I     M     H     O
# 那么现在的规律是row_id为0时填充该column，row_id 达到上限后开始递减，直到一后又开始递增。
# 我可以建立一个标识，当标识为正数时，column_id 不变化。标识为负数时，column_id发生变化。
# 如果不考虑空白的话，都不用考虑column_id，只需考虑row_id的变化就OK了
# 我要做两个方案，第一个不考虑空白，第二个填充空白并打印。
# 2015-09-08 10:43

# 拉屎时想了下，其实两种方案都不用column_id参数，所以我还是只做一种带空白的方案好了。
# 需要考虑numRows为1的特殊情况

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        print，在leetcode上运行会导致内存溢出
        因为加了一个填充空白的for循环，运行时间也会溢出。
        但是节目效果是棒的！
        """
        agent_dict = {}
        for i in range(numRows):
            agent_dict[i] = []

        total_walk = 0
        current_row = 0
        row_index = 1

        while total_walk < len(s):

            if current_row <= 0:  # 行号回到定点，方向改变
                current_row = 0
                row_index = 1

            char = s[total_walk]
            agent_dict[current_row].append(char)
            total_walk += 1

            if row_index == -1:   # 反向的时候，添加空白
                for row_id in agent_dict.keys():
                    if row_id != current_row:
                        agent_dict[row_id].append(' ')

            if current_row == numRows - 1: # 行号达到限制，方向改变
                row_index = -1
            current_row += row_index

        final_str = ''
        for row_id in sorted(agent_dict.keys()):
            row_content = ''.join(agent_dict[row_id])
            print row_content
            final_str += row_content

        final_str = final_str.replace(' ', '')
        return final_str

class SolutionAccepted_1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        不考虑columnd_id, 无空白

        1158 / 1158 test cases passed.
        Status: Accepted
        Runtime: 176 ms
        Submitted: 0 minutes ago
        """
        agent_dict = {}
        for i in range(numRows):
            agent_dict[i] = []

        total_walk = 0
        current_row = 0
        row_index = 1

        while total_walk < len(s):

            if current_row <= 0:  # 行号回到定点，方向改变
                current_row = 0
                row_index = 1

            char = s[total_walk]
            agent_dict[current_row].append(char)
            total_walk += 1

            if current_row == numRows - 1: # 行号达到限制，方向改变
                row_index = -1
            current_row += row_index

        final_str = ''
        for row_id in sorted(agent_dict.keys()):
            row_content = ''.join(agent_dict[row_id])
            final_str += row_content

        final_str = final_str.replace(' ', '')
        return final_str



class SolutionFailed_1(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        agent_dict = {}
        for i in range(numRows):
            agent_dict[i] = []

        total_walk = 0
        current_row = 0
        current_column = 0

        while total_walk < len(s):
            char = s[total_walk]

            # 当前行号超过限制的行数时，行号置零，列数增加1
            if current_row > numRows - 1:   # 此处需要减1是因为current_row的第一行用0作为序号
                current_row = 0
                current_column += 1

            if current_column % 2 == 0:     # 偶数column
                sig = 1
            else:                           # 奇数column
                if numRows == 2:
                    sig = 1
                elif numRows % 2 == 0:      # 偶数numRows的zigzag空白规则
                    if current_row % 2 != 0:
                        sig = 0
                    else:
                        sig = 1
                else:                       # 奇数numRows的zigzag空白规则
                    if current_row % 2 == 0:
                        sig = 0
                    else:
                        sig = 1

            if sig == 1:
                agent_dict[current_row].append(char)
                total_walk += 1
            elif sig == 0:
                agent_dict[current_row].append(" ")

            # 每次填充字符完毕后，row number 需要增加
            current_row += 1

        final_str = ''
        for row_id in sorted(agent_dict.keys()):
            row_content = ''.join(agent_dict[row_id])
            final_str += row_content

        final_str = final_str.replace(' ', '')
        return final_str
