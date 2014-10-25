# A def function which containing a yield is called generator-FUNCTION
# The object returned by calling this function is a generator-ITERATOR

# An iterable is an object that has an __iter__ method which returns an iterator,
# or which defines a __getitem__ method that can take sequential indexes -
# starting from zero (and raises an IndexError when the indexes are no longer valid).
# So an iterable is an object that you can get an iterator from.
# An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

# To master yield, you must understand that when you call the function,
# the code you have written in the function body does not run.

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

for i in flatten([1,[2],[[3]]]):
    print i

1
2
3





















def advance_flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in advance_flatten(sublist):
                yield element
    except TypeError:
        yield nested
