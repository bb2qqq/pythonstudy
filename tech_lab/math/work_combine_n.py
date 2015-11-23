def combine_n(elements, r, cur_index=0, cur_combo=()):
    r-=1
    temp_list = []
    for elem_index in range(cur_index, len(elements)-r):
        i = elements[elem_index]
        if r > 0:
            temp_list = temp_list + combine_n(elements, r, elem_index+1, cur_combo+(i,))
        else:
            temp_list.append(cur_combo+(i,))
    return temp_list

def all_combineation(elements):
    """ 从elements元素里取任意n个不同元素，返回所有不重复组合的列表"""
    element_length = len(elements)
    L = []
    for i in range(1, element_length+1):
        L.extend(combine_n(elements, i))
    return L
