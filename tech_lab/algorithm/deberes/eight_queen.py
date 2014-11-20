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


for x in xrange(1,9):
    for y in xrange(1,9):
        init = (x,y)
        process[init] = [init]

for init in process:
    for x in xrange(1,9):
        for y in xrange(1,9):
            for element in process[init]:
                if is_diagonal((x,y), element) or is_rect((x,y), element):
                    break
            else:
                process[init].append((x,y))

for item in process:
    print process[item]

