import random

def run(scale=0):
    L = range(100)
    d = {}
    for i in xrange(100000*(2**scale)):
        n = random.choice(L)
        if n in d:
            d[n] += 1
        else:
            d[n] = 1

    for n in sorted(d.keys()):
        print n, d[n]

    max_n = max(d.values())
    min_n = min(d.values())

    print 'min:', min_n
    print 'max:', max_n

run()
