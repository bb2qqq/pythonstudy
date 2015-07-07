# coding: utf-8
""" 一些常用的小工具 """

from datetime import datetime
import sys

import jieba


def yahoo_exchange_rate(pair='USDCNY'):
    """ 打印所查询的货币组合的实时汇率相关信息，并以浮点数形式返回汇率。
        汇率参数形式是"货币1缩写货币2缩写", 默认的汇率参数是美元对人民币。
        查询货币组合汇率不存在返回None。
        此接口为yahoo免费实时汇率的url接口，每月使用限制次数不详，有Url变动风险。
        更多yahoo汇率api信息，请移步:
        http://stackoverflow.com/questions/3139879/how-do-i-get-currency-exchange-rates-via-an-api-such-as-google-finance/16408368#16408368
    """
    import urllib
    import xml.etree.ElementTree as ET
    target_url = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20%28%22{currency_pair}%22%29&env=store://datatables.org/alltableswithkeys'
    url = urllib.urlopen(target_url.format(currency_pair=pair))
    result = url.read()
    root = ET.fromstring(result)
    query_rate = None

    for child in root:
        for grandson in child:
            for great_grandson in grandson:
                tag_name = great_grandson.tag
                tag_value = great_grandson.text
                print tag_name, tag_value
                if tag_name == 'Rate' and tag_value != 'N/A':
                    query_rate = tag_value

    return float(query_rate)


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
