# coding: utf-8
"""

Description:
    Given a winning P for team A in single match, try find the winning P for team A in a Win-X-match-in-total-Y-matches-Serie.

"""

# 我们先穷尽所有可能的结果组合。
# 然后在所有结果组合里寻找胜利超过X场的结果。
# 所以，先求一个C-Y-X的组合数，从Y场比赛里挑出X场作为获胜场次，其他为失败场次。
# 然后将该组合数乘以(P^X)*((1-P)^(Y-X))
# 接着我们求C-Y-(X+1)的组合数，乘以相应的概率。
# 最后，我们求C-Y-Y的组合数，乘以相应的概率

# 此处，我想到一点，赢了X场后，哪怕后面还有比赛，也不用打了，系列赛结束。
# 那么我们计算C-Y-Y会不会导致误差？
# 我认为是不会的。比如一个人连赢X场，比赛结束，此种情况的概率是P^X。
# 假设我们让比赛继续，连赢四场之后发生的所有比赛可能结果的总概率加起来，也还是P^X

# 看出问题了，如果是7局1胜制，现在计算得出的是7局里有任意一场获胜的概率，但事实上，第一局输了后。后面就不能再玩儿了。
# 我试了下s.serie_winning_P(0.8, 1000, 800), 结果是0.5189，这明显不对啊。。。。。
# 等等，貌似这是对的。以0.8的胜率，参加一个1000赛800胜获胜的系列赛，赢得系列赛的可能性是0.518，非常合理，我们可以推断，随着1000和800基数的增大（比例保持5比4），这个胜率会无限逼近于0.5
# 接下来我需要理解一个有点对抗直觉的事实，那就是s.serie_winning_P(0.8, 5, 4) = 0.73728
# WTF! 单场胜率0.8的意思，不就是打10局，期望能赢8场，输两场吗？也可以理解为，打5场，期望能赢4场，输一场吗？
# 而现在这个0.73728的意思是，选手打五场，输掉两场或以上的可能性是0.27 ？
# 那么，随着基数的增大（比例保持5比4），如10000赛8000胜，玩家输掉超过20%比赛场次的概率越来越接近于50%？这个又代表了什么呢？
# 玩家比赛10000场比赛，他期望的获胜数是8000场。最终他获胜低于8000场的几率无限逼近于50%。
# 也就是说在一个系列赛里，如果获胜所需场次与总场次之比等于你的单场胜率，
# 当获胜场次所需场次和总场次的值接近无限大时，此时玩家的实际获胜场次大于等于胜利所需获胜场次的概率，向下无限逼近于0.5（大于0.5）。
# 而当所需获胜场次和总场次基数很小的时候，玩家系列赛获胜的概率会明显高于0.5
# 我操，让我冷静一会儿。不敢相信！我要爆炸了
# 我靠，如果我出生在哥伦布告诉我地球是圆的那个年代，我该怎么活？


from decimal import Decimal

class Solution(object):
    """ 此处输入值太大时会导致浮点数乘以long型整数报错，可以考虑用math或其他方法优化。
        一种处理方法是将所有数字转换成decimal实例，最后再用float转回来
        浮点数乘方太多次会变成0，这个时候我们需要numpy..
        numpy.float128(0.8)
        但是
    """
    def serie_winning_P(self, single_P, winning_require_matches, max_matches):
        """ 输入： 单场胜率， 胜利所需场次，最大比赛场次
            返回： 该人在X局Y胜系列赛里获胜的概率
        """
        winning_P = 0
        if max_matches < winning_require_matches:
            return 0
        if winning_require_matches == 0:
            return 1
        for sample_n in range(winning_require_matches, max_matches+1):
            sample_combination_P = self.single_combination_P(single_P, sample_n, max_matches)
            winning_P += sample_combination_P

        return float(winning_P)

    def single_combination_P(self, single_P, sample_n, max_matches):
        """ 输入：单场胜率， 样本数，总数
            返回：该人比赛总数场次，胜利场次正好是样本数的几率
        """
        combinations = self.combinate(sample_n, max_matches)
        if sample_n != max_matches:
            sample_P = (Decimal(single_P)**sample_n) * ((Decimal(1-single_P))**(max_matches-sample_n))
        else:
            sample_P = Decimal(single_P)**sample_n
        final_P = sample_P*Decimal(combinations)
        return final_P


    def combinate(self, sample_n, total_n):
        """ 输入： 样本数，总数
            返回： 组合数
        """
        return self.factorial(total_n)/(self.factorial(sample_n)*self.factorial(total_n - sample_n))

    def factorial(self, n):
        x = 1
        for i in range(1, n+1):
            x *= i
        return x
