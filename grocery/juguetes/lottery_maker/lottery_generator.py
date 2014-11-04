import random
def give_me_number(x1=35, x2=35, n1=6, n2=1):
    L1 = range(1, x1+1)
    L2 = range(1, x2+1)

    for i in range(n1):
        proxy = random.SystemRandom()
        chosen_number = proxy.choice(L1)
        del L1[L1.index(chosen_number)]
        print chosen_number

    for i in range(n2):
        proxy = random.SystemRandom()
        chosen_number = proxy.choice(L2)
        del L2[L2.index(chosen_number)]
        print chosen_number

def super_lottery():
    print 'Super Lottery'
    give_me_number(35, 12, 5, 2)

def double_color_ball():
    print 'Double color ball'
    give_me_number(33, 16)

#super_lottery()
double_color_ball()
