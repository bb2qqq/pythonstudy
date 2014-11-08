
import time
d={}
def x(n):
    st = time.time()

    z = (2**(10*n))

    y = z ** z
    et = time.time()
    ct = et - st

    d[n] = ct
