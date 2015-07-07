1.    一瓶洗洁精，每次用到x%时，就往里面加满水，问第n次加水后，该洗洁精的原液比例是多少？加多少次水后，原液比例会小于10%？
答：./answers/dishwashing.py

2. Find the 2 numbers(non-identical) which have the smallest value difference in a list of numbers
** solution1: **

    def smallest_value_diff(target_list):
        """ 找出目标列表中差值最小的两个数字的组合 """
        cur_diff = float('inf')
        result = None
        for n1 in target_list:
            for n2 in target_list:
                if n1 != n2:
                    i1 = target_list.index(n1)
                    i2 = target_list.index(n2)
                    diff = abs(n1 - n2)
                    if diff < cur_diff:
                        cur_diff = diff
                        result = [(n1, n2, i1, i2)]
                    elif diff == cur_diff:
                        result.append((n1, n2, i1, i2))
        return result

3. 给定一个无序列表，对其进行排序
** solution1 **
def hgd_sort_1(target_list):
    """ 震惊世界的侯氏算法一代 """
    result = []
    while target_list:
        for num in target_list:
            for num_2 in target_list:
                if num < num_2:
                    break
            else:
                result.append(num)
                break
        del target_list[target_list.index(num)]
    return result

4. 写出一个脚本，这个脚本的作用是把自己的全部代码打印出来

