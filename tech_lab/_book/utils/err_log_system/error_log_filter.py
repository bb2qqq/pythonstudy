import re
import datetime

p = re.compile(r'method=.*?&')
p2 = re.compile(r'method=.*?&')
current_date = str(datetime.datetime.today())

def analyze(file_name):
    current_file = open('%s' % file_name, 'r')
    count_dict = {}
    for i in current_file:
        if 'http1connection:' not in i:
            method = p.search(i)
            if method:
                method = method.group()
                method = method.rstrip('&')
                method = method.lstrip('method=')
            else:
                method = i
        else:
            method = 'http1connection:'

        if method in count_dict:
            count_dict[method] += 1
        else:
            count_dict[method] = 1

    print '\n', file_name
    ranked_methods = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for method_name, count_time in ranked_methods:
        print method_name, count_time

print '\n\n', current_date
analyze('uncaught_log')
analyze('pure_500')
