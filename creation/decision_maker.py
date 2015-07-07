# coding: utf-8
import random

print "输入所有选项后输入q加回车退出。权重值越高说明你越希望该事件发生"
decision_pool = []

while True:
    user_input = raw_input('请输入你要决定的事件:')
    if user_input == 'q':
        break
    weight = raw_input('请输入事件"%s"的权重, 权重应当为正整数:' % user_input)
    weight = abs(int(weight))
    for i in xrange(weight):
        decision_pool.append(user_input)

your_choice = random.choice(decision_pool)
print '你选择 %s' % your_choice
