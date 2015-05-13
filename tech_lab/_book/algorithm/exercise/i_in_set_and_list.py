import time
def func1(n):
    st = time.time()
    L = range(n*n*n)
    for i in L:
        if i in L:
            pass
    et = time.time()
    print 'i in list', et - st

def func2(n):
    st = time.time()
    L = range(n*n*n)
    S = set(L)
    for i in L:
        if i in S:
            pass
    et = time.time()
    print 'i in set', et - st

func1(30)
func2(30)
