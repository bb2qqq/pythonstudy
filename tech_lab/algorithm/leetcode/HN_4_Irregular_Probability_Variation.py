"""
Design a function, which returns True or False in a random way.
Which requires:
1. The total distribution of True&False is irregular and unpredicatable(Won't fixed on a ratio even after a huge number of tests.
2. Run this function two times with same parameters will get totally different results.
"""

# The average Dice Probs decides the total distributions.
# So we Requires The Average Dice Probs changes in an uncontrollable way.
# We made distribution shift to True, then shift to False in a mild or drastic way.
# Chaos is what comes to my mind
# I need to reread <An introduction to Complexity>
import random
import math


def toss_coin(times, true_times=0, count=0, seed=random.random(),
    switch_num=random.random(), vary_rate=random.random()/100):

    while count < times:
        if seed >= 1 or seed <= 0.01:
            seed = random.random()
            switch_num = random.random()
            vary_rate = random.random() / 100

        count += 1
        judge_num = random.random()

        if switch_num >= 0.5 and judge_num < seed:
            true_times += 1
        if switch_num < 0.5 and judge_num > seed:
            true_times += 1

        seed = seed * (1 + vary_rate)

    false_times = times - true_times
    status = true_times >= false_times
    return true_times, false_times, status, (times, count, seed, switch_num, vary_rate)

def continue_running(info, continue_running_times):
    true_times, false_times, status, param_tuple = info
    old_times, count, seed, switch_num, vary_rate = param_tuple

    times = old_times + continue_running_times

    new_info = toss_coin(times, true_times=true_times, count=count,
        seed=seed, switch_num=switch_num, vary_rate=vary_rate)

    return new_info

def test_toss(base, times):
    more_true_times = 0
    more_false_times = 0
    for i in xrange(times):
        true_times, false_times, status, param_tuple = toss_coin(base)
        if status:
            more_true_times += 1
        else:
            more_false_times += 1
    trend = more_true_times >= more_false_times
    return more_true_times, more_false_times, trend
