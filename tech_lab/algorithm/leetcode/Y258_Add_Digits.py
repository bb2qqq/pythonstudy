# coding: utf-8

"""

Link: https://leetcode.com/problems/add-digits/


Description:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""

# 在python里，这个简直简单到爆，一个str(target_num), 再一个for 循环就出来了
# 如果不能用int呢？对于10进制表示的数字而言，我们用该数字与10的1次方，2次方，n次方相余，直到余数是自己，停止，再将每次相余的结果相加。

# 哦，不对，我没细读题目，题目要求的是一直相加直到剩下一个一位的数字。
# 那么只要重复上述的过程，直到最后字符化数字长度为1（方法1）或者数字与10的1次方相余等于自己（方法2）时停止。
#                                                                       2015-08-29 12:20

# 想到一个问题，比如13的最高位如何求？用13 % 100 只能得到13，我们需要想一个办法
# 之前想的第二种方法是有漏洞的。正确的方法是，求余成功后（需定义成功条件），原数字需要除以10后继续求余。直到余数等于自己后停止
# 所以，正确的第二种方式是，
# 1. 一个基数与10求余，每次求余后该基数除以10，产生次一级基数。
# 2. 如果次一级基数与10的余数不等于次级基数，继续下一次与10求余，并除以10产生更次一级的基数；
# 3. 直到最后一个n级基数与10的余数等于该n级基数为止。
# 4. 此时，将之前所有产生余数相加。产生一个新的数。
# 5. 如该数与10的余数不等于本身，将该数作为新的基数代入步骤1开始新一轮循环。反之，返回该数作为最终结果。

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        if len(str_num) == 1:
            return num
        else:
            agent_num = 0
            for i in str_num:
                agent_num += int(i)
            return self.addDigits(agent_num)


class Solution2(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 10 == num:
            return num
        else:
            agent_num = 0
            while not num % 10 == num:
                agent_num += num % 10
                num = num/10
            agent_num += num   # Add the last num which stops the while block
            return self.addDigits(agent_num)
