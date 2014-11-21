result = []

process = {}

def is_diagonal(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    if abs(x1-x2) == abs(y1-y2):
        return True
    else:
        return False

def is_rect(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    if x1 == x2 or y1 == y2:
        return True
    else:
        return False

def get_8_level(target):
    temp = []
    for i in target:
        if len(i) > 0:
            try:
                n += 1
                get_8_level(i)
            except:
                temp.append(i)
                return temp


for x in xrange(1,9):
    for y in xrange(1,9):
        init = (x,y)
        process[init] = {}

for init in process:
    for x in xrange(1,9):
        for y in xrange(1,9):
            new_c = (x,y)
            for element in process[init]:
                if is_diagonal(new_c, element) or is_rect(new_c, element):
                    break
            else:
                process[init].append(new_c)

#for item in process:
#    print process[item]

