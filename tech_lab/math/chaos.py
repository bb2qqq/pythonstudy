def logistic_map(R, x, n):
    for i in xrange(n):
        x = R*x*(1-x)
        print x
