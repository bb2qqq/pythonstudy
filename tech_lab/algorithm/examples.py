# divide & conquer
def multiply_range(n, m):
    print n, m
    if n == m:
        return n
    if m < n:
        return 1
    else:
        return multiply_range(n, (n+m)/2) * multiply_range((n+m)/2+1, m)

def factorial(n):
    return multiply_range(1, n)
