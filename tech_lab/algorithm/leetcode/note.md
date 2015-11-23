

## Iteration & Recursion

Iteration(迭代）将大任务分成若干小步。然后逐步依次完成。比如for循环就是一个iteration。  
而Recursion(递归）则是将所有的小步骤叠加储存在内存里，直到临界条件满足，将临界条件下的值输入堆栈区，运算得到最终结果。

让我们用两种方法来判断某个男人是否是成吉思汗的后代（拥有成吉思汗的Y染色体）

Iteration:

    for ancestor in all_his_paternal_ancestors:
        if ancestor == "Chengis Han"
            return True
            break
    else:
        return False


Recursion:

    def inquiry_father_info(person):
        if person.father.name == 'Chengis Han':
            return True
        elif person.father.name == 'None':
            return False
        else:
            return inquiry_father_info(person.father)

    inquiry_father_info(person)


我们可以看到Iteration就像摸着石头过河一样，是线性的。而Recursion实际上是在一步步进行一个小的自我复制，最后把所有步骤结合起来达到解决问题的目的。
