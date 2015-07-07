# coding: utf-8

index = 0

def multi_for_loop(obj, loop_num, start_index=0, return_data=[]):
    """ 此处的loop_num实际上也是数组的range数，即一个返回数组里有几个数 """
    obj = obj[start_index: ]  # 因为obj长度会变，所以不能用start_index来控制loop
    start_index += 1
    loop_num -= 1
    for i in obj:
        return_data.append(i)    
        print start_index, loop_num, obj
        if loop_num > 0:
            multi_for_loop(obj, loop_num, start_index, return_data) 
        else:
            print return_data
#            yield return_data

def multi_for_loop(obj, loop_num):
    loop_num -= 1
    for i in obj:
        if loop_num > 0:
            multi_for_loop(obj, loop_num) 
        else:
            print i
