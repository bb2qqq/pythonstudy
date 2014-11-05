from datetime import datetime
from copy import deepcopy
from sys import exit
import time
doubt_all = {}
doubt_log = {}
doubt_list = []
q=None
a=None

from cache import doubt_all, doubt_log, doubt_list
f = open('cache.py', 'w')

#def con(obj1, obj2):
#    d[obj1] = obj2


####################   MAIN  LOGIC  ##########################
def d(question=None):
    """ d is abbreviation for doubt
 Ay, ay, ay, people would die withoud docs after reviewing their own code after a month """

    if question:
        if doubt_all.get(question):
            q_index = doubt_list.index(question)
            return 'This question already exists, with  question index %d' % q_index

    question = question or raw_input()
    doubt_all[question] = None        # A question without answer
    doubt_list.append(q)              # make index for question
    q = question
    global q


    current_time = time.time()

    if doubt_log.keys():
        log_time_stamp = sorted(doubt_log.keys())[-1]
        sub_stamp = sorted(doubt_log[log_time_stamp].keys())[-1]
        if current_time - sub_stamp <= 1800:
            doubt_log[log_time_stamp][current_time] = question
        else:
            doubt_log[current_time] = {current_time: question}

    else:
        doubt_log[current_time] = {current_time: question}

    save()

def r(question=None):
    """ r is abbreviation for reply"""
    if not question:
        if 'q' in globals():
            question = q
        else:
            return "We don't have any questions yet"

    elif type(question) is int:
        if len(doubt_list) > question:
            question = doubt_list[question]

    elif not doubt_all.get(question):
        return "We don't have any questions yet"

    your_answer = raw_input()

    if doubt_all.get(question):
        doubt_all[question].append(your_answer)
    else:
        doubt_all[question] = [your_answer]

    a = doubt_all[question][-1]
    global a
    save()

def s(flag=None):
    """ s is abbreviation for show
    Show the last question-answer group
    if flag == 1, will show question index in doubt_list"""

    if not doubt_log:
        return 'Doubt log is empty'

    last_log_key = sorted(doubt_log.keys())[-1]
    last_datetime = str(datetime.fromtimestamp(last_log_key))[:19]

    print last_datetime, '\n'

    for sub_log_key in sorted(doubt_log[last_log_key].keys()):
        question = doubt_log[last_log_key][sub_log_key]
        answer_list = doubt_all[question]

        q_index = ''
        if flag == 1:
            q_index = doubt_list.index(question)

        print question, q_index
        if answer_list:
            for answer in answer_list:
                print answer
        print '\n'

    save()

########################  SHOW AREA   #############################
def hint():
    pass

def show_doubts():
    for doubt in doubt_all.keys():
        print doubt

def show_doubts_pair():
    for doubt in doubt_all.keys():
        print doubt,'\n', '\n'.join([i for i in doubt_all[doubt].keys()]), '\n'

def view(q1):
    if doubt_all.get(q1):
        return doubt_all[q1]
    else:
        return 'now answer for this question yet'


#######################  EXTRA FUNCS  #############################

def add(q1):
    complete_content = raw_input()
    q2 = q1 + complete_content
    doubt_all[q2] = deepcopy(doubt_all[q1])
    del doubt_all[q1]
    save()

def mod(q1):
    modify_content = raw_input()
    q2 = modify_content
    doubt_all[q2] = deepcopy(doubt_all[q1])
    del doubt_all[q1]
    save()

def rm(q1):
    del doubt_all[q1]
    save()


def b_find():
    pattern = raw_input()
    questions = doubt_all.keys()
    regex = re.compile(".*(%s).*" % pattern)
    search_result = [m.group(0) for l in questions for m in [regex.search(l)] if m]
    s = search_result
    global s
    return search_result

def save():
    f=open('cache.py', 'w')
    f.write('doubt_all=%r\ndoubt_log=%r\ndoubt_list=%r' % (doubt_all, doubt_log, doubt_list))
    f.close()

def backup():
    f=open('backup.py', 'w')
    f.write('doubt_all=%r\ndoubt_log=%r\ndoubt_list=%r' % (doubt_all, doubt_log, doubt_list))
    f.close()

def leave():
    f.close()
    exit()

# prevent cache crash when load
save()
#f.write('doubt_all=%r\ndoubt_log=%r' % (doubt_all, doubt_log))
