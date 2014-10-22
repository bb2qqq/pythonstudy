import random
max_L = []
min_L = []

def run(scale=0, rounds=1, print_sig=0, sys_sig=0):
    L = range(100)
    for round in xrange(rounds):
        d = {}

        if sys_sig:
            proxy = random.Sysrandom()
        else:
            random.seed()

        for i in xrange(100000*(2**scale)):
            if sys_sig:
                n = proxy.choice(L)
            else:
                n = random.choice(L)

            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        max_n = max(d.values())
        min_n = min(d.values())

        if print_sig:
            for n in sorted(d.keys()):
                print n, d[n]
            print 'min:', min_n
            print 'max:', max_n

        max_L.append(max_n)
        min_L.append(min_n)

    max_max = max(max_L.values())
    min_min = min(min_L.values())

    print 'max_max:', max_max
    print 'min_min:', min_min
