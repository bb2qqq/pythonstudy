# coding: utf-8
""" 一些常用的小工具 """

from datetime import datetime

import jieba

# short alias
dft = datetime.fromtimestamp


def convert_str_to_num(target_str, round_flag=False, float_flag=False, int_flag=False):
    """ 转换浮点或整数形式的字符串到数字。
        round_flag设为True开启四舍五入
        float_flag为True返回浮点数
        int_flag为True返回整数部分
        如果int_flag和float_flag同时开启，返回字符的整数部分。
    """
    target_str = str(target_str)

    if '.' in target_str:
        result = float(target_str)
        str_type = 'float'
    else:
        result = int(target_str)
        str_type = 'int'

    if round_flag and str_type == 'float':
        result = round(result)

    if float_flag:
        result = float(result)

    if int_flag:
        result = int(result)

    return result


def rank_word(file_, limit_word_num=None):
    """ 将中文文本里出现的词语按频率从高到低排序, limit_word_num决定打印出来的词语个数。
        本函数需要使用jieba模块进行分词预处理。
    """
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
