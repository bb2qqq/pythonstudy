# coding: utf-8

"""

Link: https://leetcode.com/problems/factorial-trailing-zeroes/

Description:
    Given an integer n, return the number of trailing zeroes in n!.
    Note: Your solution should be in logarithmic time complexity.

"""

# 此题我最先想到的是使用python math模块里内置的factorial功能。
# 然后用 factorial 结果去和10相余，余数为0就继续，直到余数不为0时停止。
# 相余且余数为0的次数总数就是我们想要的结果
# 但如果没有内置factorial函数呢？也很容易，我们循环range(1, n+1), 将里面的数循环相乘，就得到了一个factorial of n
#                                                                   2015-08-31 11:23

# 想到一个问题，0也是有factorial的。照上面的规则的话。0就进入无限循环了。。。可怕
# 需要加入一个额外判断。。
#                                                                   2015-08-31 11:43

# 第一个Solution 失败了，原因是超时。看来还有更聪明的办法。
# 我想到了另一个思路。要在结尾拥有一个0，你需要一个2与5相乘。
# 而在阶乘里，比如5的阶乘，乘到5时，前面已经有 1 x 2 x 3 x 4 两个偶数相乘
# 偶数乘以任何奇数都得偶数，所以在阶乘里，只要我们发现n有一个5或其的结合数（如10），我们可以认定该数的阶乘末尾会增加1个0.
# 那么我只要用num去除以5，看它有多少个5，就能推断num的factorial结尾有多少个0
# 怀着试一试的形态，我数了数factorial(300)后面的0， 74个！并不是意料中的60个！
# 为什么？我想了一下，明白了其中的道理。比如300这个元素，里面其实包含了两个5 x 2的组合
# 300 = 2 x 2 x 3 x 5 x 5, 所以在一个阶乘中加入300会使得这个阶乘结尾多出两个0.
# 所以，我需要判断的是一个阶乘里总共有多少prime factor 5，而不是拿num和5相除。
# 如何去判断一个数里有多少个prime factor 5呢？
# 拿这个数一直去整除5，能够整除的次数就是该数里prime factor 5的数量。
# 来把，试试新的solution!
#                                                                   2015-08-31 12:30

# 第二个solution又失败了，看来不能用for循环，应该还有其他的规律。。。
# 知道了，在一个数n的阶乘里，只有结尾是5或者10的数才会含有prime factor 5
# 所以该问题可以转换为，快速发现range(1, n+1)里所有结尾为5或0的数
# 在python里这是很容易的。。range(0, n+1, 5) 可以找到所有含有5和10的数
# 接下来我们需要一种比较快的方法，找到这些数里面每个数有多少个factor5
# 如果这个方法需要的是线性时间的话。我们只是把n的运行时间缩减到n/5, 但仍然是O(n)的复杂度。

# 上面提到的方法，在找出所有含有prime factor 5的元素后，还需要找到含有两个prime factor 5 的元素数量。
# 一直找到含有n个prime factor 5的元素数量为止。
# 如何找出一个数字序列里，它拥有prime factor 5数量最多的数字有几个prime factor 5 ？我陷入了思考。

# 我又拿100做了下试验，发现100里面有24个含有prime factor 5的数字。
# 为什么是24个而不是20个呢？因为像25这样的数字有两个prime factor 5
# 那么100里有几个25呢？答案是100/25 = 4. 100/25 + 100/5 = 24!
# Bingo! 用这个理论的话，125里应当含有125/(5**3) + 125/(5**2) + 125/(5**1) = 31
# 和我之前笨方法得到的结果一致！Problem solved!
#                                                                       2015-08-31 18:11

# 我去我，震惊了。用新的算法，妙解问题：
#In [7]: s.trailingZeroes(110000000000000000000000000000000000000000000000)
#Out[7]: 27499999999999999999999999999999999999999999990L
#
# 上面的运算对于最新的算法而言，是瞬间出答案。而用之前的解法，到中国队世界杯夺冠后都算不出结果。

# 我在想，现有的解法里两次运算会对运行速度造成多少影响，打算减少一次运算，增加一次赋值。
# 结果反而更慢！我不服，我要减短变量名! 再来一次
# 减短变量名后，更慢！说明leetcode的运行速度测试值会根据你的代码在某一范围内波动？
# 啊啊啊！
#                                                                       2015-08-31 18:45

class Solution(object):
    """
    502 / 502 test cases passed.
    Status: Accepted
    Runtime: 80 ms
    Submitted: 0 minutes ago

    """
    def trailingZeroes(self, n):
        p = 0
        d = 1

        r = n/(5**d)
        while r != 0:
            p += r
            d += 1
            r = n/(5**d)

        return p


class Solution_2(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        用于测试两次计算对于运算速度的影响

        502 / 502 test cases passed.
        Status: Accepted
        Runtime: 68 ms
        Submitted: 0 minutes ago
        """
        prime_factor_5_num = 0
        power_index = 1

        result = n/(5**power_index)
        while result != 0:
            prime_factor_5_num += result
            power_index += 1
            result = n/(5**power_index)

        return prime_factor_5_num


class Solution_1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int

        :result
            502 / 502 test cases passed.
            Status: Accepted
            Runtime: 64 ms
            Submitted: 0 minutes ago

        """
        prime_factor_5_num = 0
        power_index = 1

        while n/(5**power_index) != 0:
            prime_factor_5_num += n/(5**power_index)
            power_index += 1

        return prime_factor_5_num




class SolutionFailed_2(object):
    """
    Status: Time Limit Exceeded
    Submitted: 0 minutes ago
    Last executed input:
    8362

    It's better than solution1, but not good enough.
    """

    def count_prime_factor_5(self, n):
        """ Count prime factor 5 for positive intergers. 0 is not accepted."""
        prime_factor_5_num = 0
        while n/5 == n/float(5):
            prime_factor_5_num += 1
            n /= 5
        return prime_factor_5_num

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        trailing_zero_numbers = 0
        for i in range(1, n+1):
            prime_factor_5_num = self.count_prime_factor_5(i)
            trailing_zero_numbers += prime_factor_5_num
        return trailing_zero_numbers


class SolutionFailed_1(object):
    """
        Status: Time Limit Exceeded
        Submitted: 0 minutes ago
        Last executed input:
        2666

        Which means this solution is a clumsy solution
    """

    def zen_factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        factorial_n = self.zen_factorial(n)
        trailing_zero_numbers = 0

        while factorial_n % 10 == 0:
            factorial_n /= 10
            trailing_zero_numbers += 1
        return trailing_zero_numbers
