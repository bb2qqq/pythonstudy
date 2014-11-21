# coding:utf-8
import datetime
import sys
from English_cache import raw_dict


# Automatically load new words
def init():
    f=open('raw', 'r')
    for i in f:
        i = i.rstrip('\n')
        i = i.split('-')
        if len(i) >= 2:
            En = i[0]
            Es = i[1]
            if En in raw_dict:
                if raw_dict[En].get('spanish'):
                    pass
                else:
                    raw_dict[En]['spanish'] = Es
            else:
                raw_dict[En] = { 'meaning': '', 'synonym': [], 'spanish': Es, 'relative_word':[], 'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now()}
    save()


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
                'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now()}
    save()

def wash_ass(target_dict):
    for old_word in target_dict:
        if type(raw_dict[old_word]) is list:
            try:
                if len(raw_dict[old_word]) == 7:
                    meaning, synonym, spanish, forget_score, pronounciation, relative_word, word_type = raw_dict[old_word]
                else:
                    meaning, synonym, spanish, forget_score, pronounciation, relative_word, = raw_dict[old_word]
            except:
                print raw_dict[old_word]
                sys.exit(0)
            target_dict[old_word] = {}
            target_dict[old_word]['meaning'] = meaning
            target_dict[old_word]['synonym'] = synonym
            target_dict[old_word]['spanish'] = spanish
            target_dict[old_word]['forget_score'] = forget_score
            target_dict[old_word]['pronounciation'] = pronounciation
            target_dict[old_word]['relative_word'] = relative_word
    save()

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
        word_type =  raw_input("Enter the Word_Type below and press ENTER when finished typing:\n\n")
        try:
            if word_type not in raw_dict[old_word].get('word_type'):
                raw_dict[old_word].get('word_type').append(word_type)
        except:
            raw_dict[old_word]['word_type'] = [word_type]
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def g(old_word=''):
    'short for get'
    old_word = old_word or raw_input('Enter the word:')
    if old_word in raw_dict:
        meaning = raw_dict[old_word].get('meaning')
        synonym = raw_dict[old_word].get('synonym')
        spanish = raw_dict[old_word].get('spanish')
        forget_score = raw_dict[old_word].get('forget_score')
        pronounciation = raw_dict[old_word].get('pronounciation')
        relative_word = raw_dict[old_word].get('relative_word')
        word_type = raw_dict[old_word].get('word_type')
        create_time = raw_dict[old_word].get('create_time')


        print old_word
        print 'meaning:', meaning
        if synonym:
            print 'synonym:', synonym
        if spanish:
            print 'spanish:', spanish
        if forget_score:
            print 'forget_score:', forget_score
        if pronounciation:
            print 'pronounciation:', convert(pronounciation)
        if relative_word:
            print 'relative_word:', relative_word
        if word_type:
            print 'word_type:', word_type
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."

def convert(pronounciation):
    return pronounciation.replace('Z','ð').replace('SH','ʃ').replace('S','s').replace('J','ʒ').replace('G','dʒ').replace('CH','tʃ').replace('E','ə').replace('A','ʌ').replace('O','ɔ').replace('N','ŋ')

def e():
    'short for español if you are in EnglishDict, short for english if you are in SpanishDict'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        spanish =  raw_input("Enter the Spanish below and press ENTER when finished typing:\n\n")
        raw_dict[old_word]['spanish'] = spanish
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def m():
    'short for meaning'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        if raw_dict[old_word].get('meaning'):
            confirm = raw_input('The current meaning is: %s, press y to continue, press other to quit\n'  % raw_dict[old_word].get('meaning'))
            if confirm == 'y':
                meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")
                raw_dict[old_word]['meaning'] = meaning
        else:
            meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")
            raw_dict[old_word]['meaning'] = meaning
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def s():
    'short for synonym'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        synonym =  raw_input("Enter the Synonym below and press ENTER when finished typing:\n\n")
        raw_dict[old_word].get('synonym').append(synonym)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def r():
    'short for relative words'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        relative_word =  raw_input("Enter the Relative_Word below and press ENTER when finished typing:\n\n")
        if relative_word not in raw_dict[old_word].get('relative_word'):
            raw_dict[old_word].get('relative_word').append(relative_word)
        if raw_dict.get(relative_word):
            if old_word not in raw_dict[relative_word]['relative_word']:
                raw_input[relative_word]['relative_word'].append(old_word)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def p():
    'short for pronounciation, for ENGLISH word only'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        pronounciation =  raw_input("Enter the Pronounciation below and press ENTER when finished typing:\n\n")
        raw_dict[old_word]['pronounciation'] = pronounciation
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def f(score=1,):
    """short for forget, default score is 1, if you want to lower a word\'s socre, just pass negative number to this func"""
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        raw_dict[old_word]['forget_score'] += score
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def v(rev=True, SS=False, L2=False, T=False ):
    """Short for view, default to rank from the word you forgot the most times, pass any value to rank from reverse
    L2 = bilingual, SS = show score, rev = Reverse, T = by time order
    """
    if not SS:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else raw_dict[x].get('forget_score') , reverse = rev):
            if L2:
                if not raw_dict[i].get('spanish'):
                    continue
            print i
    else:
        for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else raw_dict[x].get('forget_score'), reverse = rev):
            if L2:
                if not raw_dict[i].get('spanish'):
                    continue
            print i, raw_dict[i].get('forget_score')

def h():
    """ show IPA(International Phonetic Alphabet) mapping """
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
    f.write('import datetime\nraw_dict=%r' % raw_dict)
    f.close()

def se(quit_sig=False):
    ' short for save exit, actually it is often used for backup'
    f = open('English_backup.py', 'a')
    now = str(datetime.datetime.now())[:19]
    f.write('\nlast_time=%r\n' % now)
    f.write('raw_dict=%r\n' % raw_dict)
    f.close()
    if quit_sig:
        sys.exit(0)

def exam(rev=True, L2=False, T=False ):
    """Default to rank from the word you forgot the most times, pass any value to rank from reverse
    L2 = bilingual, rev = Reverse, T = by time order,
    """

    for i in sorted(raw_dict.keys(), key=lambda x: raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else raw_dict[x].get('forget_score') , reverse = rev):
        if L2:
            if not raw_dict[i].get('spanish'):
                continue

        if L2:
            print '\n'
            print 'Please type the Spanish/English version of: ', i
            answer = raw_input('>>>')
            if answer == raw_dict[i]['spanish']:
                raw_dict[i]['forget_score'] -= 1
            else:
                raw_dict[i]['forget_score'] += 1
                print '\n'
                g(old_word=i)

        else:
            print '\n'
            print 'Do you remember: ',i, '?'
            answer = raw_input('type y for yes, and others for no: ')
            if answer == 'y' or answer == 'yes':
                raw_dict[i]['forget_score'] -= 1
            else:
                raw_dict[i]['forget_score'] += 1
                print '\n'
                g(old_word=i)

init()
