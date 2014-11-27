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
            category = []
            word_type = ''
            if len(i) >=3:
                category = i[2]
            if len(i) >=4:
                word_type = i[3]
            if En in raw_dict:
                if raw_dict[En].get('spanish'):
                    pass
                else:
                    raw_dict[En]['spanish'] = Es
            else:
                raw_dict[En] = { 'meaning': '', 'synonym': [], 'spanish': Es, 'relative_word':[], 'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now(),  'category': []}
            if category and 'category' in raw_dict[En] and category not in raw_dict[En]['category']:
                raw_dict[En]['category'].append(category)
            if word_type:
                if word_type not in raw_dict[En].get('word_type', []):
                    raw_dict[En]['word_type'].append(word_type)
    save()


def a():
    'short for add'
    new_word = raw_input('Enter the word:')
    if new_word in raw_dict:
        print 'The word you are trying to add is already in the dict, please use other methods to modify it.'    # do something here
    else:
        meaning = raw_input("Enter the Meaning below and press ENTER when finished typing:\n\n")
        if not new_word:
            return
        word_type = raw_input('\nEnter the word type, please:\n')
        raw_dict[new_word] = { 'meaning': meaning, 'synonym': [], 'spanish': '', 'relative_word':[],
                'pronounciation':'', 'word_type': [word_type], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': []}
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
                raw_dict[old_word]['word_type'].append(word_type)
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
        category = raw_dict[old_word].get('category')

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
        if category:
            print 'category', category
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

        if relative_word in raw_dict:
            if 'relative_word' in raw_dict[relative_word]:
                if old_word in raw_dict.get('relative_word', []):
                    pass
                else:
                    raw_dict[relative_word]['relative_word'].append(old_word)
            else:
                raw_dict[relative_word]['relative_word'] = [old_word]
        else:
            raw_dict[relative_word] = { 'meaning': '', 'synonym': [], 'english': '', 'relative_word':[old_word],
                    'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [] }


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

def v(rev=True, SS=False, L2=False, T=False, wt='', cat='', sl=0, exam=0):
    """Short for view, default to rank from the word you forgot the most times, pass any value to rank from reverse
    L2 = bilingual, SS = show score, rev = Reverse, T = by time order, wt = by word type, cat = by category, sl = score limit
    """
    target = sort_by_score(raw_dict.keys(), rev=rev, sl=sl)

    if T:
        target = sort_by_time(target)

    if L2:
        target = sort_by_bilingual(target)

    if wt:
        target = sort_by_word_type(target, wt)

    if cat:
        target = sort_by_category(target, cat)

    if exam:
        return target

    if not SS:
        for i in target:
            print i
    else:
        for i in target:
            print i, raw_dict[i].get('forget_score')


def sort_by_score(target, rev, sl):
    temp_L = []
    target = sorted(target, key=lambda x: raw_dict[x].get('forget_score', 0), reverse = rev)
    if sl:
        for i in target:
            i_score = raw_dict[i].get('forget_score', 0)
            if i >= sl:
                temp_L.append(i)
        return temp_L
    return target

def sort_by_bilingual(target):
    temp_L = []
    for i in target:
        if raw_dict[i].get('spanish'):
            temp_L.append(i)
    return temp_L

def sort_by_time(target):
    target = sorted(target, key=lambda x: raw_dict[x].setdefault('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)))
    return target

def sort_by_word_type(target, word_type):
    temp_L = []
    for i in target:
        if word_type in raw_dict[i].get('word_type', []):
            temp_L.append(i)
    return temp_L

def sort_by_category(target, category):
    temp_L = []
    for i in target:
        if category in raw_dict[i].get('category', []):
            temp_L.append(i)
    return temp_L

def h():
    """Short for help, show IPA(International Phonetic Alphabet) mapping """
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

    f2 = open('E_mobile', 'w')
    target = v(exam=1)
    for i in target:
        word = i
        meaning = raw_dict[i].get('meaning', '')
        spanish = raw_dict[i].get('spanish', '')
        word_type = raw_dict[i].get('word_type', '')
        forget_score = raw_dict[i].get('forget_score', 0)
        pronounciation = raw_dict[i].get('pronounciation', '')
        if spanish:
            spanish=' <' + spanish + '>'
        if not word_type:
            word_type=''
        if pronounciation:
            pronounciation = ' [' + pronounciation + ']'
        if meaning:
            meaning =  '   \"' + meaning + '\"'

        f2.write('{word}  {spanish}{pronounciation}{meaning}\n'.format(word=word,  spanish=spanish, meaning=meaning, pronounciation=pronounciation))
    f2.close()


def se(quit_sig=False):
    ' short for save exit, actually it is often used for backup'
    f = open('English_backup.py', 'a')
    now = str(datetime.datetime.now())[:19]
    f.write('\nlast_time=%r\n' % now)
    f.write('raw_dict=%r\n' % raw_dict)
    f.close()
    if quit_sig:
        sys.exit(0)

def exam(rev=True, L2=False, T=False, target = []):
    """Default to rank from the word you forgot the most times, pass any value to rank from reverse
    L2 = bilingual, rev = Reverse, T = by time order, you can use v() to pass a filtered target list to exam()
    """
    target = target or sorted(raw_dict.keys(), key=lambda x: raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else raw_dict[x].get('forget_score') , reverse = rev)

    temp_L = []

    for i in target:
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
                temp_L.append(i)
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
                temp_L.append(i)
                print '\n'
                g(old_word=i)

    if temp_L:
        print 'These are the words you failed in this exam, you can put more effort on them later.\n'
        for i in temp_L:
            print '\t\t', i

    save()

def get_current_category():
    L = []
    for i in raw_dict:
        if raw_dict[i].get('category'):
            L.extend([raw_dict[i]['category']])

    S = set(L)

    return (" ").join([i for i in S])

def c():
    """ Short for category """
    # this function can
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        if raw_dict[old_word].get('category'):
            print 'Current categories for this word:', '\t'.join(raw_dict[old_word]['category']), '. Type y to add new category, type others to quit'
            choice = raw_input('>>>')
            if choice not in ['y', 'yes']:
                return
            else:
                current_category = get_current_category()
                print "Current exists categories are: ", current_category
                category =  raw_input("Enter your category below and press ENTER when finished typing:\n\n")
                raw_dict[old_word].setdefault['category'] = category
        else:
            raw_dict[old_word]['category'] = []
            current_category = get_current_category()
            print "Current exists categories are: ", current_category
            category =  raw_input("Enter your category below and press ENTER when finished typing:\n\n")
            raw_dict[old_word].setdefault['category'] = category

    else:
        print " The word you are searching for is not in this dict now, please check your spelling."

    save()


init()
