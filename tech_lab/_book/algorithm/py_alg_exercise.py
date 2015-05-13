# 1-1.
"""
_Consider the following statement: "As machines get faster and memory cheaper, algorithms become less important." What do you think; is this true or false? Why?_
"""

# my answer:
"""
    The data scale will rise up together with hardware improvement. Before we are dealing with files at MB level.
    Now we are dealing with TB level files. So algorithm is still very important, and even more important than before.
"""


# 1-2.
""" Find a way of checking whether two strings are anagrams of each other (such as "debit card" and "bad credit")
How well do you think your soltuion scales?
Can you think of a naive solution that will scale very poorly?
"""

#my answer:

# 1.
def find_anagram(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))
# 2.
# Not efficient enough, but acceptable, actually I don't know how it scales.

# 3. Yes, I can.
def naive_find_anagram(word1, word2):

    from copy import deepcopy
    list1 = list(word1)
    list2 = list(word2)
    cp_list1 = deepcopy(list1)
    cp_list2 = deepcopy(list2)

    for char in word1:
        if char in word2:
# NOT FINISHED
