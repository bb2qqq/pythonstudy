# Build and return a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))

# the function above is not acceptable when the interger is huge.
# inmagine doing firstn(1000000000000000), how much memory do you need ?

# Here we comes the generator solution:

# Using the generator pattern (an iterable)
class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn(1000000))

# This will perform as we expect, but we have the following issues:
#    >> there is a lot of boilerplate
#    >> the logic has to be expressed in somewhat convoluted way
# Furthermore, this is a pattern that we will use over and over for many similar constructs
# Imagine writing all that just to get an iterator.

# Python provides generator functions as a convinient shortcut to building iterators.

# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))

class Bank(object):
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'

class BigBank(object):
    crisis = False
    def create_atm(self):
        while not self.crisis:
            return '$100'




