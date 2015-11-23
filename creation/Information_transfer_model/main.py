# coding: utf-8
"""
"""
import random
import sys
import time
import signal
from threading import Thread

# 我很自然地想到了用数字之间的间隔来表示人与人之间在地理上的区隔。
# 如 1 和 3 对于2而言是最亲密的数字，可以差不多看成是直系亲属。
# 对象之间的互相引用，我们可以用一个字典来做索引。
#                                               2015-09-06 15:55
OBJECT_DICT = {}
NOTIFIED_LIST = []
UNIT_NUMS = 10000  # 用于实验的实例对象

RUNNING_TIME = 15  # 在首次信息发送多少秒后结束程序运行，查看结果
POSSIBLE_CONTACT_RANGE = range(500)  # 一个人能接触到的离他最远的人离他的可能距离, 此值应小于UNIT_NUMS的一半，因为表示的是一个对象向左右展开的范围
POSSIBLE_CONTACT_NUM = range(20)  # 一个人分享重要信息对象数的可能区间范围
POSSIBLE_CONTACT_INTERVAL = range(5)  # 一个人分享信息的最大可能时间间隔, 在此48的值是玩家定义的时间单位



# 为了方便统计，我们把每一个单元用类抽象出来，在初始化时传入id
# 我们首先需要生成一个消息，以及它的时间, 或者消息本身就是时间戳！
# 接着我们需要一个分享信息的method，叫它exchange好了
# tell会决定信息分享的时间频率，分享人数和范围
#                                               2015-09-06 16:32

class BasicUnit(object):
    def __init__(self, id_):
        self.id_ = id_
        self.msg = None
        self.receive_time = None
        self.contact_range = random.choice(POSSIBLE_CONTACT_RANGE)
        self.contact_num = random.choice(POSSIBLE_CONTACT_NUM)
        self.contact_interval = random.choice(POSSIBLE_CONTACT_INTERVAL)

    def get_reachable_contacts(self):
        """ 辅助method, 用于获得某个单元的可接触单元列表。可接触元素向两边展开"""

        # 此处reach
        reach_end = self.id_ + self.contact_range > UNIT_NUMS
        reach_start = self.id_ - self.contact_range < 0

        if reach_end and reach_start:
            print "ERROR! CONTACT RANGE EXCEED UNIT NUMS!!!"
            sys.exit(1)
        elif reach_start:
            reachable_contacts = range(self.contact_range*2 + 1)
        elif reach_end:
            reachable_contacts = range(UNIT_NUMS - self.contact_range*2 - 1, UNIT_NUMS)
        else:
            reachable_contacts = range(self.id_ - self.contact_range, self.id_ + self.contact_range + 1)

        reachable_contacts.remove(self.id_)
        return reachable_contacts


    def exchange(self, msg):
        if self.msg == msg:
            return

        NOTIFIED_LIST.append(self.id_)
        self.msg = msg
        self.receive_time = time.time()
        actual_contact_num = min(self.contact_num, self.contact_range)  # 有可能随机出range小于num的情况，此处进行自动修正
        reachable_contacts = self.get_reachable_contacts()
        chosen_contact_units = random.sample(reachable_contacts, actual_contact_num)

        # TODO 此处应引入多线程
        for target_unit in chosen_contact_units:
            if self.contact_interval:  # 有interval的值可能为0
                time.sleep(random.choice(range(self.contact_interval)))

            target_obj = OBJECT_DICT[target_unit]
            thread_obj = Thread(target=target_obj.exchange, args=(msg,))
            thread_obj.start()


# 此处加入最终统计逻辑
def alarm_function(*params):
    got_msg_units = 0
    total_waiting_time = 0
    for obj in OBJECT_DICT.values():
        if obj.msg:
            got_msg_units += 1
            total_waiting_time += obj.receive_time - obj.msg

    average_waiting_time = total_waiting_time/got_msg_units

    print "got_msg_units:", got_msg_units
    print "average_waiting_time:", average_waiting_time
#    sys.exit(0)

# 如果我定期的加入alarm，然后在alarm函数里加入写入数据库的功能。我就能从数据库里读到实时统计数据了！
signal.signal(signal.SIGALRM, alarm_function)
#signal.alarm(RUNNING_TIME)

# 我们最后要模拟的，是在一个自定义的时间范围内， 在不同的参数下，一个信息覆盖了多少的人群
for i in range(UNIT_NUMS):
    OBJECT_DICT[i] = BasicUnit(id_=i)

starter = random.choice(range(UNIT_NUMS))
OBJECT_DICT[starter].exchange(time.time())
