from sys import argv
num_limit = int(argv[1])
import copy
from datetime import datetime, timedelta
import time
mix_uid_dict = {}
mix_money_dict = {}


st = time.time()
platform_dict = {}
with open('/data/opt/sites/zengjuchen/lab/basic/dataware/ios_pay_all' , 'r') as f:
    for i in f:
        i = i.rstrip('\n')
        i = i.split('\t')
        try:
            money = int(i[6])
        except:
            continue
        uid = i[13]
        date = i[7][:10]
        platform = i[8]

        if 'admin' not in platform :
            if 1:
                if date in mix_uid_dict:
                    if uid not in mix_uid_dict[date]:
                        mix_uid_dict[date].append(uid)
                elif date not in mix_uid_dict:
                    mix_uid_dict[date] = [uid]

                if date in mix_money_dict:
                    mix_money_dict[date] += money
                elif date not in mix_money_dict:
                    mix_money_dict[date] = money

                platform_dict[uid] = platform

mix_uniq_uid_dict = copy.deepcopy(mix_uid_dict)

for date in sorted(mix_uid_dict.keys(), key = lambda x: datetime.strptime(x,'%Y-%m-%d'),):
    next_day = str(datetime.strptime(date,'%Y-%m-%d') + timedelta(days=1))[:10]
    if next_day in mix_uid_dict:
        mix_uniq_uid_dict[next_day].extend(mix_uniq_uid_dict[date])
        mix_uniq_uid_dict[next_day] = list(set(mix_uniq_uid_dict[next_day]))

mix_each_day_uid_dict = {}
for date in  mix_uid_dict.keys():
    mix_each_day_uid_dict[date] = set()


for date in mix_uid_dict:
    mix_uid_dict[date] = set(mix_uid_dict[date])

for date in mix_uniq_uid_dict:
    mix_uniq_uid_dict[date] = set(mix_uniq_uid_dict[date])

for date in sorted(mix_uid_dict.keys(), key = lambda x: datetime.strptime(x,'%Y-%m-%d'),) :
    previous_day = str(datetime.strptime(date,'%Y-%m-%d') - timedelta(days=1))[:10]
    if previous_day in mix_uid_dict:
        for uid in mix_uid_dict[date]:
            if uid not in mix_uniq_uid_dict[previous_day]:
                mix_each_day_uid_dict[date].update([uid])

count = 0
for date in sorted(mix_uid_dict.keys(), key = lambda x: datetime.strptime(x,'%Y-%m-%d'), reverse=True) :
    if count < num_limit:
        for uid in mix_each_day_uid_dict[date]:
            print date, '\t', uid, '\t', uid[0], '\t', platform_dict[uid]
        count += 1

et = time.time()

print et - st
