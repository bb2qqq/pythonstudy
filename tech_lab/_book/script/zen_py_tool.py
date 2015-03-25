# coding: utf-8
from datetime import datetime

import jieba

# short alias
dft = datetime.fromtimestamp

def rank_word(file_, limit_word_num=None):
    """ 将中文文本里出现的词语按频率从高到低排序"""
    agent_list = []
    agent_dict = {}
    for line in file_:
        # 将所有行连成一个字符串，防止换行将一个词语切开
        line=line.rstrip('\n')
        agent_list.append(line)

    whole_text_str = ''.join(agent_list)

    sliced_word_list = jieba.cut(whole_text_str)
    for word in sliced_word_list:
        if word in agent_dict:
            agent_dict[word] += 1
        else:
            agent_dict[word] = 1

    ranked_list = sorted(agent_dict.items(), key=lambda x: x[1], reverse=True)

    printed_num = 0
    for word, rank in ranked_list:
        if not limit_word_num or printed_num < limit_word_num:
            print  word, '\t', rank
            printed_num += 1
