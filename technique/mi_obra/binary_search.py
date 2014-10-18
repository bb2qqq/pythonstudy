L = [1,4,5]

def bs(seq, num, lower_limit=0, up_limit=None):
    """ find the pos of a num in a sorted list """
    if up_limit == None:
        up_limit = len(seq) - 1

    print lower_limit, up_limit

    mid = (up_limit + lower_limit)//2

    if num == seq[mid]:
        return mid

    if up_limit - lower_limit == 1:
        if num != seq[mid]:
            print 'This num is not in sequence, the closest number is on position:'
            if abs(seq[up_limit] - num) < abs(seq[lower_limit] - num):
                return up_limit
            elif abs(seq[up_limit] - num) > abs(seq[lower_limit] - num):
                return lower_limit
            else:
                return lower_limit, 'and', up_limit

    if num > seq[mid]:
        return bs(seq, num, mid, up_limit)
    elif num < seq[mid]:
        return bs(seq, num, lower_limit, mid)
