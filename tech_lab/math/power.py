# coding: utf-8
def explore_power_increase_speed(round_=20):
    """ 探索n ** n 增长的速度 """
    # 结论，数值一直在以加速度增长，不过加速度越来越小，趋向于匀速增长
    result = []

    for i in xrange(round_):
        n = i + 1
        n2 = i + 2
        power_i = i**i
        power_n = n**n
        power_n2 = n2**n2

        try:
            power_i, power_n, power_n2 = map(float, [power_i, power_n, power_n2])
        except:
            pass

        increase_times = power_n/power_i    # n 开 n 次方是 n-1 开 n-1次方的值的多少倍
        next_increase_times = power_n2/power_n  # n+1 开 n+1 次方是 n 开 n 次方的值的多少倍
        n2_i_compare = power_n2/power_i  # n+1 开 n+1 次方是 n-1 开 n-1 次方的多少倍
        next_accelarated_times = next_increase_times - increase_times  # 倍速增长绝对值
        times_increase_speed = float(next_increase_times/increase_times)  # 倍数增长的速度
        result.append((increase_times, next_accelarated_times, n2_i_compare, times_increase_speed))

    for increase_times, next_accelarated_times, n2_i_compare, times_increase_speed in result:
        print increase_times, '\t', next_accelarated_times, '\t', n2_i_compare, '\t', times_increase_speed

explore_power_increase_speed()
