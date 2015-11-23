""" 调整origin_value, valve_value, change_rate, symbol 来获取你独特的波浪图案！ """

import time
import random

def graphic_print(n):
    x = int(n * 50)
    print  symbol * x

origin_value = 0.02
valve_value = 0.3
change_rate = 1.1
symbol = " 你最棒 "


sleep_time = origin_value
while True:
    graphic_print(sleep_time)
    time.sleep(sleep_time)

    if sleep_time >= valve_value:
        back_sig = True
    elif sleep_time == origin_value or abs(origin_value / sleep_time - 1) <= 0.01:
        back_sig = False

    if sleep_time < valve_value and not back_sig:
        sleep_time *= change_rate
    elif back_sig:
        sleep_time /= change_rate

