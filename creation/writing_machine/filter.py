# coding: utf-8
""" 根据SogouLabDic.dic 文件生成python格式的字典文件"""

base_dict = {}
genre_set = set([])
genre_dict = {}

with open("SogouLabDic.dic", 'r') as f:
    for i in f:
        try:
            i = i.rstrip('\n')
            i = i.split()
            if len(i) > 2:
                word, value,  genres = i
                genre_list = genres.split(',')
                genre_set.update(genre_list)
            else:
                word, value = i
                genre_list = []

            word = word.decode('gb2312')  # 将gb2312字符转化为unicode
            value = int(value)
            base_dict[word] = {'value': value, 'genre': genre_list}

            for genre in genre_list:
                if genre in genre_dict:
                    genre_dict[genre].update({word: value})
                else:
                    genre_dict[genre] = {word: value}

        except:
            pass

with open('TEMPZ_base_dict.py', 'w') as f:
    f.write('TEMPZ_base_dict=%r\n' % base_dict)
    f.write('TEMPZ_genre_dict=%r\n' % genre_dict)
