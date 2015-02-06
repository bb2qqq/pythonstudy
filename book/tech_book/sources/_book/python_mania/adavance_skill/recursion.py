def factorial(n):
    if n == 1:
        return 1
    else:
        print locals()                       # for debug
        return n * factorial(n-1)

def power(x,n):
    for i in range(n-1):
        x *= x
    return x
