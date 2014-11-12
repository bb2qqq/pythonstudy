from Spanish_cache import raw_dict
import datetime

def a():
    'short for add'
    new_word = raw_input('Enter the word:')
    if new_word in raw_dict:
        pass    # do something here
    else:
        meaning = raw_input("Enter the Meaning below and press ENTER when finished typing:\n\n")
        raw_dict[new_word] = [meaning, [], '', 0, '' ]
    save()

def g():
    'short for get'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        meaning, synonym, english, forgot_time, pronounciation  = raw_dict[old_word]
        print old_word, ':'
        print 'meaning:', meaning
        if synonym:
            print 'synonym:', synonym
        if english:
            print 'english:', english
        if forgot_time:
            print 'forgot_time:', forgot_time
        if pronounciation:
            print 'pronounciation:', pronounciation
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."

def e():
    'short for español'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        english =  raw_input("Enter the Spanish below and press ENTER when finished typing:\n\n")
        raw_dict[old_word][2] = english
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def s():
    'short for synonym'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        synonym =  raw_input("Enter the Synonym below and press ENTER when finished typing:\n\n")
        raw_dict[old_word][1].append(synonym)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def p():
    'short for pronounciation, for English word only'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        pronounciation =  raw_input("Enter the Pronounciation below and press ENTER when finished typing:\n\n")
        raw_dict[old_word][2] = pronounciation
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()
def f(score=1):
    'short for forget, default score is 1'
    old_word = raw_input('Enter the word:')
    """ use it when you forget the word """
    if old_word in raw_dict:
        raw_dict[old_word][3] += score
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def v(reverse_sig=0, withscores=0):
    """Short for view, default to rank from the word you forgot the highest time, pass any value to rank from reverse """
    if not withscores:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x][3], reverse= not reverse_sig):
            print i
    else:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x][3], reverse= not reverse_sig):
            print i, raw_dict[i][3]

def save():
    f = open('Spanish_cache.py', 'w')
    f.write('raw_dict=%r' % raw_dict)
    f.close()

def se():
    ' short for save exit '
    f = open('Spanish_backup.py', 'a')
    now = str(datetime.datetime.now())[:19]
    f.write('\nlast_time=%s\n' % now)
    f.write('raw_dict=%r\n' % raw_dict)
    f.close()
