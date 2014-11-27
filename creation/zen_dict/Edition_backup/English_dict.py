# coding:utf-8
from English_cache import raw_dict
import datetime

def a():
    'short for add'
    new_word = raw_input('Enter the word:')
    if new_word in raw_dict:
        pass    # do something here
    else:
        meaning = raw_input("Enter the Meaning below and press ENTER when finished typing:\n\n")
        if not new_word:
            return
        type = raw_input('\nEnter the word type, please:\n')
        raw_dict[new_word] = { 'meaning': meaning, 'synonym': [], 'spanish': '', 'relative_word':[],
                               'pronounciation':'', 'type': [], 'forget_score': 0}
        raw_dict[new_word] = [meaning, [], '', 0, '', [], [type]]
    save()

def wash_ass(target_dict):
    for i in target_dict:
        if type(i) is list:
            pass  # do something here.

def d():
    'short for del'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        raw_dict.pop(old_word)    # do something here
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def t():
    'short for type'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        type =  raw_input("Enter the Type below and press ENTER when finished typing:\n\n")
        try:
            if type not in raw_dict[old_word][6]:
                raw_dict[old_word][6].append(type)
        except:
            raw_dict[old_word].append([type])
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def g():
    'short for get'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        try:
            meaning, synonym, spanish, forgot_time, pronounciation, relative_word, type = raw_dict[old_word]
        except:
            raw_dict[old_word].append([])
            meaning, synonym, spanish, forgot_time, pronounciation, relative_word, type = raw_dict[old_word]

        print old_word
        print 'meaning:', meaning
        if synonym:
            print 'synonym:', synonym
        if spanish:
            print 'spanish:', spanish
        if forgot_time:
            print 'forgot_time:', forgot_time
        if pronounciation:
            print 'pronounciation:', convert(pronounciation)
        if relative_word:
            print 'relative_word:', relative_word
        if type:
            print 'type:', type
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."

def convert(pronounciation):
    return pronounciation.replace('Z','ð').replace('SH','ʃ').replace('S','s').replace('J','ʒ').replace('G','dʒ').replace('CH','tʃ').replace('E','ə').replace('A','ʌ').replace('O','ɔ').replace('N','ŋ')

def e():
    'short for español if you are in EnglishDict, short for english if you are in SpanishDict'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        spanish =  raw_input("Enter the Spanish below and press ENTER when finished typing:\n\n")
        raw_dict[old_word][2] = spanish
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def m():
    'short for meaning'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        if raw_dict[old_word][0]:
            confirm = raw_input('The current meaning is: %s, press y to continue, press other to quit\n'  % raw_dict[old_word][0])
            if confirm == 'y':
                meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")
                raw_dict[old_word][0] = meaning
        else:
            meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")
            raw_dict[old_word][0] = meaning
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

def r():
    'short for relative words'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        relative_word =  raw_input("Enter the Relative_Word below and press ENTER when finished typing:\n\n")
        if relative_word not in raw_dict[old_word][5]:
            raw_dict[old_word][5].append(relative_word)
        if raw_dict.get(relative_word):
            if old_word not in raw_dict[relative_word][5]:
                raw_input[relative_word][5].append(old_word)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def p():
    'short for pronounciation, for ENGLISH word only'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        pronounciation =  raw_input("Enter the Pronounciation below and press ENTER when finished typing:\n\n")
        raw_dict[old_word][4] = pronounciation
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

def v(reverse_sig=0, withscores=0, L2=0):
    """Short for view, default to rank from the word you forgot the highest time, pass any value to rank from reverse """
    if not withscores:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x][3], reverse= not reverse_sig):
            if L2:
                if not raw_dict[i][2]:
                    continue
            print i
    else:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x][3], reverse= not reverse_sig):
            if L2:
                if not raw_dict[i][2]:
                    continue
            print i, raw_dict[i][3]

def h():
    print """
              E for ə
              A for ʌ
              O for ɔ
              J for ʒ
             SH for ʃ
              N for ŋ
              S for θ
              Z for ð
             CH for tʃ
              G for dʒ
          """

def save():
    f = open('English_cache.py', 'w')
    f.write('raw_dict=%r' % raw_dict)
    f.close()

def se():
    ' short for save exit '
    f = open('English_backup.py', 'a')
    now = str(datetime.datetime.now())[:19]
    f.write('\nlast_time=%r\n' % now)
    f.write('raw_dict=%r\n' % raw_dict)
    f.close()
