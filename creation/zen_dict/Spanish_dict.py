# coding:utf-8
import sys
from Spanish_cache import raw_dict, score, st_dict
import datetime

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
            if Es in raw_dict:
                if raw_dict[Es].get('english'):
                    pass
                else:
                    raw_dict[Es]['english'] = En
            else:
                raw_dict[Es] = { 'meaning': '', 'synonym': [], 'english': En, 'relative_word':[], 'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': []}
            if category and 'category' in raw_dict[Es] and category not in raw_dict[En]['category']:
                raw_dict[Es]['category'].append(category)
            if word_type:
                if word_type not in raw_dict[Es].get('word_type', []):
                    raw_dict[Es]['word_type'].append(word_type)
    save()


def a(b=0):
    'short for add, b is short for bilingual'
    new_word = raw_input('Enter the word:')
    new_word = spanish_convert(new_word)
    if new_word:
        add_score()

    if new_word in raw_dict:
        print 'The word you are trying to add is already in the dict, please use other methods to modify it.'    # do something here
    else:
        meaning = raw_input("Enter the Meaning below and press ENTER when finished typing:\n\n")
        meaning = spanish_convert(meaning)
        if not new_word:
            return
        english = raw_input('\nEnter the English corresponde word, please:\n')


        word_type = raw_input('\nEnter the word type, please:\n')
        category = raw_input('\nEnter the category, please:\n')

        if meaning:
            add_score(3)
        if english:
            add_score()
        if word_type:
            add_score(0.5)
        if category:
            add_score(0.5)

        raw_dict[new_word] = { 'meaning': meaning, 'synonym': [], 'english': english, 'relative_word':[],
                'pronounciation':'', 'word_type': [word_type], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [category] }

        # When bilingual signal is True, create new world in the correspond dict.
    if b:
        from English_cache import raw_dict as english_raw_dict, score as english_score, st_dict as english_st_dict
        if english and english not in english_raw_dict:
            english_raw_dict[english] = { 'meaning': '', 'synonym': [], 'spanish': new_word, 'relative_word':[],
            'pronounciation':'', 'word_type': [word_type], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [category]}

            f = open('English_cache.py', 'w')
            f.write('import datetime\nraw_dict=%r\nscore=%d\nst_dict=%r' % (english_raw_dict, english_score, english_st_dict))
            f.close()

    save()

def b(new_word=''):
    """ b is short to make a word in bilingual dict(in both English dict and Spanish dict)"""

    new_word = new_word or raw_input('Please enter the word you want to transfer:\n')

    if new_word not in raw_dict:
        print 'The word does not exist in this dict'
        return
    elif not raw_dict[new_word].get('english'):
        print 'You did not add spanish correspondents for this word!'
        return
    else:
        pass

    meaning, synonym, english, forget_score, pronounciation, relative_word, word_type, create_time, category = g(new_word, data=True)


    from English_cache import raw_dict as english_raw_dict, score as english_score, st_dict as english_st_dict
    if english and english not in english_raw_dict:
        english_raw_dict[english] = { 'meaning': '', 'synonym': synonym, 'english': new_word, 'relative_word': relative_word, 'pronounciation':pronounciation, 'word_type': word_type, 'forget_score': forget_score, 'create_time': datetime.datetime.now(), 'category': category}

        f = open('English_cache.py', 'w')
        f.write('import datetime\nraw_dict=%r\nscore=%d\nst_dict=%r' % (english_raw_dict, english_score, english_st_dict))
        f.close()
    else:
        print "That word is already in the target dictionary!"
        return


    save()


def spanish_convert(target):
    """  In case you don't have spanish input on your machine, you can use a,e,i,o,u + ' to add stress, and n + ~ to convert it to ñ """
    target = target.replace("a'",'á',).replace("e'",'é',).replace("i'",'í',).replace("o'",'ó',).replace("u'",'ú',).replace("n~",'ñ',)
    return target

def wash_ass(target_dict):
    for old_word in target_dict:
        if type(raw_dict[old_word]) is list:
            try:
                if len(raw_dict[old_word]) == 7:
                    meaning, synonym, english, forget_score, pronounciation, relative_word, word_type = raw_dict[old_word]
                else:
                    meaning, synonym, english, forget_score, pronounciation, relative_word, = raw_dict[old_word]
            except:
                print raw_dict[old_word]
                sys.exit(0)
            target_dict[old_word] = {}
            target_dict[old_word]['meaning'] = meaning
            target_dict[old_word]['synonym'] = synonym
            target_dict[old_word]['english'] = english
            target_dict[old_word]['forget_score'] = forget_score
            target_dict[old_word]['pronounciation'] = pronounciation
            target_dict[old_word]['relative_word'] = relative_word
    save()

def d():
    'short for del'
    old_word = raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        temp_score = 0
        for item in raw_dict[old_word]:
            if raw_dict[old_word][item]:
                temp_score += 1
        add_score(-temp_score)
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
        finally:
            add_score(0.5)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def g(old_word='', data=False):
    'short for get, data is the sig to demand return data of a word'
    old_word = old_word or raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        meaning = raw_dict[old_word].get('meaning')
        meaning = spanish_convert(meaning)

        synonym = raw_dict[old_word].get('synonym')
        english = raw_dict[old_word].get('english')
        forget_score = raw_dict[old_word].get('forget_score')
        pronounciation = raw_dict[old_word].get('pronounciation')
        relative_word = raw_dict[old_word].get('relative_word')
        word_type = raw_dict[old_word].get('word_type')

        create_time = raw_dict[old_word].get('create_time')
        category = raw_dict[old_word].get('category')

        print old_word
        print 'meaning:', meaning

        # signal to demand return data
        if data:
            return meaning, synonym, english, forget_score, pronounciation, relative_word, word_type, create_time, category

        if synonym:
            print 'synonym:', synonym
        if english:
            print 'english:', english
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
    return pronounciation.replace('Z','ð').replace('SH','ʃ').replace('S','θ').replace('J','ʒ').replace('G','dʒ').replace('CH','tʃ').replace('E','ə').replace('A','ʌ').replace('O','ɔ').replace('N','ŋ')

def e(b=0):
    'short for español if you are in EnglishDict, short for english if you are in SpanishDict'
    old_word = raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        english =  raw_input("Enter the English below and press ENTER when finished typing:\n\n")

        raw_dict[old_word]['english'] = english
        add_score()

        if b:
            from English_cache import raw_dict as english_raw_dict, score as english_score
            if english and english not in english_raw_dict:
                word_type = raw_dict[old_word].get('word_type', [])
                category = raw_dict[old_word].get('category', [])
                english_raw_dict[english] = { 'meaning': '', 'synonym': [], 'spanish': old_word, 'relative_word':[],
                'pronounciation':'', 'word_type': word_type, 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': category}

                f = open('English_cache.py', 'w')
                f.write('import datetime\nraw_dict=%r\nscore=%d' % (english_raw_dict, english_score))
                f.close()

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
                meaning = spanish_convert(meaning)
                raw_dict[old_word]['meaning'] = meaning
                add_score(0.5)
        else:
            meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")
            meaning = spanish_convert(meaning)
            raw_dict[old_word]['meaning'] = meaning
            add_score(3)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def s():
    'short for synonym'
    old_word = raw_input('Enter the word:')
    if old_word in raw_dict:
        synonym =  raw_input("Enter the Synonym below and press ENTER when finished typing:\n\n")
        synonym = spanish_convert(synonym)
        raw_dict[old_word].get('synonym').append(synonym)
        add_score()
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def r(nc=0):
    'short for relative words, nc stands for no clone, which means do not try to make new word of the typing relative word'
    old_word = raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        relative_word =  raw_input("Enter the Relative_Word below and press ENTER when finished typing:\n\n")
        relative_word = spanish_convert(relative_word)
        if relative_word not in raw_dict[old_word].get('relative_word'):
            raw_dict[old_word].get('relative_word').append(relative_word)
            add_score()

        if raw_dict.get(relative_word):
            if old_word not in raw_dict[relative_word]['relative_word']:
                raw_dict[relative_word]['relative_word'].append(old_word)

        if nc:
            return

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
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        pronounciation =  raw_input("Enter the Pronounciation below and press ENTER when finished typing:\n\n")
        raw_dict[old_word]['pronounciation'] = pronounciation
        add_score(1.5)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."
    save()

def f(score=1,):
    """short for forget, default score is 1, if you want to lower a word\'s socre, just pass negative number to this func"""
    old_word = raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
    if old_word in raw_dict:
        raw_dict[old_word]['forget_score'] += score
        add_score(-2)
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
        if raw_dict[i].get('english'):
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
    f = open('Spanish_cache.py', 'w')
    f.write('import datetime\nraw_dict=%r\nscore=%d\nst_dict=%r' % (raw_dict, score, st_dict))
    f.close()

    f2 = open('S_mobile', 'w')
    target = v(exam=1)
    for i in target:
        word = i
        meaning = raw_dict[i].get('meaning', '')
        english = raw_dict[i].get('english', '')
        word_type = raw_dict[i].get('word_type', '')
        forget_score = raw_dict[i].get('forget_score', 0)
        pronounciation = raw_dict[i].get('pronounciation', '')
        if english:
            english=' <' + english + '>'
        if not word_type:
            word_type=''
        if pronounciation:      # No pronounciation for Spanish mobile version
            pronounciation = ' [' + pronounciation + ']'
        if meaning:
            meaning =  '   \"' + meaning + '\"'

        f2.write('{word}  {english}{meaning}\n'.format(word=word,  english=english, meaning=meaning))
    f2.close()


def se(quit_sig=False):
    ' short for save exit, actually it is often used for backup'
    f = open('Spanish_backup.py', 'a')
    now = str(datetime.datetime.now())[:19]
    f.write('\nlast_time=%r\n' % now)
    f.write('raw_dict=%r\n' % raw_dict)
    f.write('score=%r\n' % score)
    f.write('st_dict=%r\n' % st_dict)
    f.close()
    if quit_sig:
        sys.exit(0)

def exam(rev=True, L2=False, T=False, target = [], st=False ):
    """Default to rank from the word you forgot the most times, pass any value to rank from reverse
    L2 = bilingual, rev = Reverse, T = by time order, st = test sentence, you can use v() to pass a filtered target list to exam()
    """

    # sentence test begin

    if st:
        agent = show_st(exam=True)
        for index, sentence in agent:
            print sentence, '\n'
            answer = raw_input('Recuerdas este frase?')
            if answer in ['y', 'yes', 's', 'si']:
                st_dict[index]['forget_score'] -= 1
                add_score(1)
            else:
                st_dict[index]['forget_score'] += 1
                add_score(-2)
        save()
        return

    # sentence test end

    target = target or sorted(raw_dict.keys(), key=lambda x: raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else raw_dict[x].get('forget_score') , reverse = rev)

    temp_L = []

    for i in target:
        if L2:
            if not raw_dict[i].get('english'):
                continue

        if L2:
            print '\n'
            print 'Please type the Spanish/English version of: ', i
            answer = raw_input('>>>')
            answer = spanish_convert(answer)
            if answer == raw_dict[i]['english']:
                raw_dict[i]['forget_score'] -= 1
                add_score(1)
                print '\n'
                g(old_word=i)
            else:
                raw_dict[i]['forget_score'] += 1
                add_score(-2)
                temp_L.append(i)
                print '\n'
                g(old_word=i)
                print '\n'

        else:
            print '\n'
            print 'Recuerdas este?   ',i
            answer = raw_input('type y for yes, and others for no: ')
            answer = spanish_convert(answer)
            if answer in ['y', 'yes', 's', 'si']:
                raw_dict[i]['forget_score'] -= 1
                add_score(1)
                print '\n'
                g(old_word=i)
            else:
                raw_dict[i]['forget_score'] += 1
                add_score(-2)
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
        category = raw_dict[i].get('category')
        if category:
            if type(category) == list:
                L.extend(raw_dict[i]['category'])
            elif type(category) == str:
                L.append(raw_dict[i]['category'])

    S = set(L)

    return ("\t").join([i for i in S])

def c():
    """ Short for category """
    old_word = raw_input('Enter the word:')
    old_word = spanish_convert(old_word)
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
                if not category in raw_dict[old_word]['category']:
                    raw_dict[old_word].setdefault['category'] = category
                add_score(0.5)
        else:
            raw_dict[old_word]['category'] = []
            current_category = get_current_category()
            print "Current exists categories are: ", current_category
            category =  raw_input("Enter your category below and press ENTER when finished typing:\n\n")
            raw_dict[old_word].setdefault['category'] = category
            add_score(0.5)
    else:
        print " The word you are searching for is not in this dict now, please check your spelling."

    save()

def vc():
    """ short for view category """
    result =  get_current_category()
    return result

def add_score(num=1):
    global score
    score += num

def x():
    'x is short for experience'
    print "TU PUNTO: ", score

def show_init_score():   # single-use function
    temp_score = 0
    for word in raw_dict:
        for item in raw_dict[word]:
            if raw_dict[word][item]:
                temp_score += 1
    print temp_score

def init_exam():
    n = 0
    x = 0
    for i in raw_dict:
        score = raw_dict[i].get('forget_score', 0)
        if score >= 1:
            n += 1
        if score == 0:
            x += 1
    if n > 15 or x > 20:
        print "\n\n\n\n\n AHORA TIENES MAS DE %d PALABRAS OLVIDOS Y %d PALABRAS DESMEMORIZADOS, HAGA EL EXAMEN POR FAVOR  \n\n\n\n\n" %(n,x)

        choice = raw_input("HAGA EL EXAMEN AHORA?")

        if choice in ['y', 'yes', 's', 'sí', 'OK', 'vale', 'fine']:
            exam()

    else:
        pass
#        print "\nDE TODO MODO VAS A TOMAR ETSE EXAMEN, DISFRUTALO!"
#        exam()

def st(d=False):
    """ short for sentence, d = delete signal """
    used_index = set(st_dict.keys())
    index_pool = set(range(100000))
    usable_index = index_pool - used_index
    next_index = sorted(list(usable_index))[0]
    sentence = raw_input('please type the sentence below:\n\n')

    exist_sentence = set([x['sentence'] for x in st_dict.values()])

    if sentence not in exist_sentence:
        st_dict[next_index] = {'forget_score': 0, 'sentence': sentence}

    save()

def show_st(exam=False):

    temp = []
    for index in sorted(st_dict.keys(), key=lambda x: st_dict[x]['forget_score']):
        sentence = st_dict[index]['sentence']

        if not exam:
            print 'index: ', index,'\n'
            print sentence, '\n\n'

        else:
            temp.append((index, sentence))

    if exam:
        return temp


init()
init_exam()
