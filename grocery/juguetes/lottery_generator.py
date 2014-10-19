import random
def give_me_number(x1=35, x2=35, n1=6, n2=1):
    L1 = range(1, x1+1)
    L2 = range(1, x2+1)

    for i in range(n1):
        chosen_number = random.choice(L1)
        del L1[L1.index(chosen_number)]
        print chosen_number

    for i in range(n2):
        chosen_number = random.choice(L2)
        del L2[L2.index(chosen_number)]
        print chosen_number

give_me_number(35, 12, 5, 2)
