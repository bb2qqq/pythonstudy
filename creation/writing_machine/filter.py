# coding: utf-8

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

with open('base_dict.py', 'w') as f:
    f.write('base_dict=%r\n' % base_dict)
    f.write('genre_dict=%r\n' % genre_dict)
