# what do we want: to say the deepest level of a dict
# what do we have, all the elements of the dict


def nested_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1
    return 1 + max(nested_depth(v) for v in d.values())





def recur(my_dict):
    wr_n = 0
    try:
        for item in my_dict:
            wr_n += 1
            recur(item)
    except:
        wr_n += 1
        pass

    if wr_n == len(my_dict.keys()):
        return my_dict
