# coding: utf-8
import random
def ban_shi():
    your_word=raw_input("你:")
    if your_word == '我爸是那谁谁':
        print '好的，您先坐会，马上就好！'
        return
    else:
        excuse=random.choice(['对不起，按规定这个不能办。', '我们现在不办公，下个星期二再来吧。', '星期二我们内部交流，不对外办公。',
                '你找XX局吧。', '你的证件不齐。', '这不是我们负责范围', '我们只接受网上预约。', '我们网上预约系统坏了，你过几天再来吧。'])
        print '工作人员: ', excuse
        ban_shi()




def my_recur(target):
    target -= 1
    if target == 1:
        print 'if'
    else:
        print 'else'
        return my_recur(target)
