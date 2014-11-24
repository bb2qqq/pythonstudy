# what do we want: to say the deepest level of a dict
# what do we have, all the elements of the dict


def recur(my_dict):
    wr_n = 0
    try:
        for item in my_dict:
            recur(item)
    except:
        wr_n += 1
        pass

    if wr_n == len(my_dict.keys()):
        yield result







def get_dict_level(target):
    n = 0
    if target.keys():
        n += 1
        for i in target.keys():
            if get_dict_level(i):
                n += 1

    print n













































