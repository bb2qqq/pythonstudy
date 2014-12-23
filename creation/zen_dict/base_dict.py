# coding:utf-8
import sys
from sys import argv
import datetime
import pickle
import random
import importlib
import pprint

try:
    sig = argv[1]
except:
    sig = ''

""" 现在的问题，每次改动时都需要对比改动两个文件，比较麻烦, 希望可以做一个模板词典，支持任意个语言之间的通用化。 当然，需要将之前版本的数据导入确保读档时不会初始化对象 """
def get_dict(first_lan='', second_lan='', transfer=False):
    """ Using for check if target_dict exists, if not, make one, else, get it. All dict name are represent in English. """
    global __doc__

    first_lan = first_lan or raw_input('Please type in the first language of the dict:\n')
    second_lan = second_lan or raw_input('Please type in the second language of the dict:\n')
    avail_language = ['Spanish', 'English', 'Chinese', 'French', 'German', 'Arabic', 'Russian', 'Portuguese', 'Japanese', 'Korean', 'Italian', 'Hindi']
    if first_lan not in avail_language or second_lan not in avail_language:
        print 'The language you typed in is not supported by this dict system, please select from the following list, if you still have doubts, try contact marioykuky@gmail.com'
        pprint.pprint(avail_language)
        get_dict()

    __doc__ += '\n This is a %s_%s_dict made by you and zen_dict system ' %  (first_lan, second_lan)


    # compatibility with old code
    if transfer:
        if first_lan == 'English' and second_lan == 'Spanish':
            agent = importlib.import_module('English_cache')

        if first_lan == 'Spanish' and second_lan == 'English':
            agent = importlib.import_module('Spanish_cache')

        current_dict = BaseDict(first_lan, second_lan, agent.raw_dict, agent.score, agent.st_dict, wash_ass=True)

    else:
        try:
            agent = importlib.import_module('%s_%s_cache' % (first_lan, second_lan))
            current_dict = pickle.loads(agent.__dict__['%s_%s_cache' % (first_lan, second_lan)])
        except:
            print 'exept happend'
            current_dict = BaseDict(first_lan, second_lan, {}, 0, {})

    globals().update({'a': current_dict.a, 'b': current_dict.b, 'd': current_dict.d, 't': current_dict.t,
                    'g': current_dict.g, 'sl': current_dict.sl, 'm': current_dict.m, 's': current_dict.s,
                    'r': current_dict.r, 'p': current_dict.p, 'f': current_dict.f, 'v': current_dict.v,
                    'h': current_dict.h,  'c': current_dict.c, 'x': current_dict.x, 'se': current_dict.se,
                    'exam': current_dict.exam, 'save': current_dict.save, 'raw_dict': current_dict.raw_dict,
                     })

    print __doc__

    return current_dict



class BaseDict(object):
    def __init__(self, first_lan, second_lan, raw_dict, score, st_dict, wash_ass=False):
        self.first_lan = first_lan
        self.second_lan = second_lan
        self.raw_dict = raw_dict
        self.score = score
        self.st_dict = st_dict
        self.exam_rate = 30

        self.__dict__.update({})    # make abbreviation for methods, make the code more readable, preserved for now

        if wash_ass:
            self.wash_ass()

        if first_lan in ['English', 'Spanish']:
            self.init()

        self.init_exam()


    # 将原数据结构里的spanish和english转为sl_word
    def wash_ass(self):
        for word in self.raw_dict:
            if 'spanish' in self.raw_dict[word]:
                self.raw_dict[word]['sl_word'] = self.raw_dict[word]['spanish']
                del self.raw_dict[word]['spanish']

            if 'english' in self.raw_dict[word]:
                self.raw_dict[word]['sl_word'] = self.raw_dict[word]['english']
                del self.raw_dict[word]['english']

        self.save()

    # Automatically load new words in a brief file
    def init(self):
        f=open('raw', 'r')
        for i in f:
            i = i.rstrip('\n')
            i = i.split('-')
            if len(i) >= 2:
                if self.first_lan == 'English':
                    En = i[0]
                    Es = i[1]
                if self.first_lan == 'Spanish':     # still En is i[0], this is a tricky to keep other structure unmodified
                    En = i[1]
                    Es = i[0]

                category = []
                word_type = ''
                if len(i) >=3:
                    category = i[2]
                if len(i) >=4:
                    word_type = i[3]
                if En in self.raw_dict:
                    if self.raw_dict[En].get('sl_word'):
                        pass
                    else:
                        self.raw_dict[En]['sl_word'] = Es
                else:
                    self.raw_dict[En] = { 'meaning': '', 'synonym': [], 'sl_word': Es, 'relative_word':[], 'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now(),  'category': []}
                try:
                    if category and 'category' in self.raw_dict[En] and category not in self.raw_dict[En]['category']:
                        self.raw_dict[En]['category'].append(category)
                    if word_type:
                        if word_type not in self.raw_dict[En].get('word_type', []):
                            self.raw_dict[En]['word_type'].append(word_type)
                except:
                    print category, word_type, 'add failes.'
        self.save()


    def a(self, b=0):
        'short for add, b is short for bilingual'
        new_word = raw_input('Enter the word:')

        if new_word in self.raw_dict:
            print 'The word you are trying to add is already in the dict, please use other methods to modify it.'    # do something here

        else:
            if new_word:
                self.add_score(1)

            if not new_word:
                print 'Your typing for new_word is empty!'
                return

            meaning = raw_input("Enter the Meaning below and press ENTER when finished typing:\n\n")

            # sl_word is short for second_language word
            sl_word = raw_input('\nEnter the %s corresponde word, please:\n' % self.second_lan)
            # spanish_convert is a special function for converting english typing to spanish, when you don't have spanish input
            if self.second_lan == 'Spanish':
                sl_word = self.spanish_convert(sl_word)

            word_type = raw_input('\nEnter the word type, please:\n')
            category = raw_input('\nEnter the category, please:\n')

            if meaning:
                self.add_score(3)
            if sl_word:
                self.add_score(1)
            if word_type:
                self.add_score(0.5)
            if category:
                self.add_score(0.5)

            self.raw_dict[new_word] = { 'meaning': meaning, 'synonym': [], 'sl_word': sl_word, 'relative_word':[],
                    'pronounciation':'', 'word_type': [word_type], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [category]}

            # When bilingual signal is True, create new world in the correspond dict.
            # ? Here comes the issue, how to call another object add the word, and save it?
        if b:
            sec_dict = get_dict(self.second_lan, self.first_lan)
            if sl_word and sl_word not in sec_dict.raw_dict:
                sec_dict.raw_dict[sl_word] = { 'meaning': '', 'synonym': [], 'sl_word': new_word, 'relative_word':[], 'pronounciation':'', 'word_type': [word_type], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [category]}
                sec_dict.save()
            else:
                print "That word is already in the target dictionary!"


        self.save()

    def b(self, new_word=''):
        """ b is short to make a word in bilingual dict(in both English dict and Spanish dict)"""

        new_word = new_word or raw_input('Please enter the word you want to transfer:\n')

        if new_word not in self.raw_dict:
            print 'The word does not exist in this dict'
            return
        elif not self.raw_dict[new_word].get('sl_word'):
            print 'You did not add sencon language word for this word!'
            return
        else:
            pass

        meaning, synonym, sl_word, forget_score, pronounciation, relative_word, word_type, create_time, category = self.g(new_word, data=True)

        sec_dict = get_dict(self.second_lan, self.first_lan)
        if sl_word and sl_word not in sec_dict.raw_dict:
            sec_dict.raw_dict[sl_word] = { 'meaning': '', 'synonym': synonym, 'english': new_word, 'relative_word': relative_word, 'pronounciation':pronounciation, 'word_type': word_type, 'forget_score': forget_score, 'create_time': datetime.datetime.now(), 'category': category}

            sec_dict.save()
        else:
            print "That word is already in the target dictionary!"

# Special word convert func starts here

    def spanish_convert(self, target):
        """  In case you don't have spanish input on your machine, you can use a,e,i,o,u + ' to add stress, and n + ~ to convert it to ñ """
        target = target.replace("a'",'á',).replace("e'",'é',).replace("i'",'í',).replace("o'",'ó',).replace("u'",'ú',).replace("n~",'ñ',)
        return target

# Special word convert func ends here


    def d(self):
        'short for del'
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            temp_score = 0
            for item in self.raw_dict[old_word]:
                if self.raw_dict[old_word][item]:
                    temp_score += 1
            self.add_score(-temp_score)
            self.raw_dict.pop(old_word)    # do something here
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."

        self.save()

    def t(self):
        'short for word type'
        old_word = raw_input('Enter the word:')
        if old_word in self.raw_dict:
            word_type =  raw_input("Enter the Word_Type below and press ENTER when finished typing:\n\n")
            try:
                if word_type not in self.raw_dict[old_word].get('word_type'):
                    self.raw_dict[old_word]['word_type'].append(word_type)
            except:
                self.raw_dict[old_word]['word_type'] = [word_type]
            finally:
                self.add_score(0.5)
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def g(self, old_word='', data=False):
        'short for get, data is the sig to demand return data of a word'
        old_word = old_word or raw_input('Enter the word:')

        if old_word in self.raw_dict:
            meaning = self.raw_dict[old_word].get('meaning')
            synonym = self.raw_dict[old_word].get('synonym')
            sl_word = self.raw_dict[old_word].get('sl_word')
            forget_score = self.raw_dict[old_word].get('forget_score')
            pronounciation = self.raw_dict[old_word].get('pronounciation')
            relative_word = self.raw_dict[old_word].get('relative_word')
            word_type = self.raw_dict[old_word].get('word_type')

            create_time = self.raw_dict[old_word].get('create_time')
            category = self.raw_dict[old_word].get('category')

            # signal to demand return data
            if data:
                return meaning, synonym, sl_word, forget_score, pronounciation, relative_word, word_type, create_time, category

            print old_word

            if meaning:
                print 'meaning:', meaning
            if synonym:
                print 'synonym:', synonym
            if sl_word:
                print 'sl_word:', sl_word
            if forget_score:
                print 'forget_score:', forget_score
            if pronounciation:
                print 'pronounciation:', self.convert(pronounciation)
            if relative_word:
                print 'relative_word:', relative_word
            if word_type:
                print 'word_type:', word_type
            if category:
                print 'category', category

        else:
            print " The word you are searching for is not in this dict now, please check your spelling."

    def convert(self, pronounciation):
        """ Convert typings for English internation phonetic marks. """
        return pronounciation.replace('Z','ð').replace('SH','ʃ').replace('S','θ').replace('J','ʒ').replace('G','dʒ').replace('CH','tʃ').replace('E','ə').replace('A','ʌ').replace('O','ɔ').replace('N','ŋ')

    def sl(self, b=0):
        'short for second language, b flag means pass this word to relative dict or not'
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            sl_word =  raw_input("Enter the Spanish below and press ENTER when finished typing:\n\n")
            if self.second_lan == 'Spanish':
                sl_word = self.spanish_convert(sl_word)
            self.raw_dict[old_word]['sl_word'] = sl_word
            self.add_score()

            #  the 1st b is flag name, 2nd b is the instance function name.
            if b:
                self.b(old_word)

        else:
            print " The word you are searching for is not in this dict now, please check your spelling."

        self.save()

    def m(self):
        'short for meaning'
        old_word = raw_input('Enter the word:')
        if old_word in self.raw_dict:
            if self.raw_dict[old_word].get('meaning'):
                confirm = raw_input('The current meaning is: %s, press y to continue, press other to quit\n'  % self.raw_dict[old_word].get('meaning'))
                if confirm == 'y':
                    meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")

                    self.raw_dict[old_word]['meaning'] = meaning
                    self.add_score(0.5)
            else:
                meaning =  raw_input("Enter the meaning below and press ENTER when finished typing:\n\n")

                self.raw_dict[old_word]['meaning'] = meaning
                self.add_score(3)
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def s(self):
        'short for synonym'
        old_word = raw_input('Enter the word:')
        if old_word in self.raw_dict:
            synonym =  raw_input("Enter the Synonym below and press ENTER when finished typing:\n\n")

            self.raw_dict[old_word].get('synonym').append(synonym)
            self.add_score()
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def r(self, nc=0):
        'short for relative words, nc stands for no clone, which means do not try to make new word of the typing relative word'
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            relative_word =  raw_input("Enter the Relative_Word below and press ENTER when finished typing:\n\n")

            if relative_word not in self.raw_dict[old_word].get('relative_word'):
                self.raw_dict[old_word].get('relative_word').append(relative_word)
                self.add_score()

            if self.raw_dict.get(relative_word):
                if old_word not in self.raw_dict[relative_word]['relative_word']:
                    self.raw_dict[relative_word]['relative_word'].append(old_word)

            if nc:
                return

            if relative_word in self.raw_dict:
                if 'relative_word' in self.raw_dict[relative_word]:
                    if old_word in self.raw_dict.get('relative_word', []):
                        pass
                    else:
                        self.raw_dict[relative_word]['relative_word'].append(old_word)
                else:
                    self.raw_dict[relative_word]['relative_word'] = [old_word]
            else:
                self.raw_dict[relative_word] = { 'meaning': '', 'synonym': [], 'english': '', 'relative_word':[old_word],
                        'pronounciation':'', 'word_type': [], 'forget_score': 0, 'create_time': datetime.datetime.now(), 'category': [] }


        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def p(self):
        'short for pronounciation, it is by default means the pronounciation of the first lan, but if first lan does not need this, like Spanish, it is refer to the second lan, and you can specify this in the object doc information'
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            pronounciation =  raw_input("Enter the Pronounciation below and press ENTER when finished typing:\n\n")
            self.raw_dict[old_word]['pronounciation'] = pronounciation
            self.add_score(1.5)
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def f(self, f_score=1):
        """short for forget, default score is 1, if you want to lower a word\'s socre, just pass negative number to this func"""
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            self.raw_dict[old_word]['forget_score'] += f_score
            self.add_score(-2)
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."
        self.save()

    def v(self, rev=True, SS=False, L2=False, T=False, wt='', cat='', sl=0, exam=0):
        """Short for view, default to rank from the word you forgot the most times, pass any value to rank from reverse
        L2 = bilingual, SS = show score, rev = Reverse, T = by time order, wt = by word type, cat = by category, sl = score limit
        """
        target = self.sort_by_score(self.raw_dict.keys(), rev=rev, sl=sl)

        if T:
            target = self.sort_by_time(target)

        if L2:
            target = self.sort_by_bilingual(target)

        if wt:
            target = self.sort_by_word_type(target, wt)

        if cat:
            target = self.sort_by_category(target, cat)

        if exam:
            return target

        if not SS:
            for i in target:
                print i
        else:
            for i in target:
                print i, self.raw_dict[i].get('forget_score')


    def sort_by_score(self, target, rev, sl):
        "sl is short for score_limit"
        temp_L = []
        target = sorted(target, key=lambda x: self.raw_dict[x].get('forget_score', 0), reverse = rev)
        if sl:
            for i in target:
                i_score = self.raw_dict[i].get('forget_score', 0)
                if i_score >= sl:
                    temp_L.append(i)
            return temp_L
        return target

    def sort_by_bilingual(self, target):
        temp_L = []
        for i in target:
            if self.raw_dict[i].get('sl_word'):
                temp_L.append(i)
        return temp_L

    def sort_by_time(self, target):
        target = sorted(target, key=lambda x: self.raw_dict[x].setdefault('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)))
        return target

    def sort_by_word_type(self, target, word_type):
        temp_L = []
        for i in target:
            if word_type in self.raw_dict[i].get('word_type', []):
                temp_L.append(i)
        return temp_L

    def sort_by_category(self, target, category):
        temp_L = []
        for i in target:
            if category in self.raw_dict[i].get('category', []):
                temp_L.append(i)
        return temp_L

    def h(self):
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

    def save(self):
        """ Emobile is a temporary solution for my study on mobiles """
        saving_data = pickle.dumps(self)
        f = open('%s_%s_cache.py' % (self.first_lan, self.second_lan), 'w')
        f.write('%s_%s_cache=%r' % (self.first_lan, self.second_lan, saving_data))
        f.close()

        f2 = open('%s_%s_mobile' % (self.first_lan, self.second_lan), 'w')
        target = self.v(exam=1)
        for i in target:
            word = i
            meaning = self.raw_dict[i].get('meaning', '')
            sl_word = self.raw_dict[i].get('sl_word', '')
            word_type = self.raw_dict[i].get('word_type', '')
            pronounciation = self.raw_dict[i].get('pronounciation', '')
            if sl_word:
                sl_word=' <' + sl_word + '>'
            if not word_type:
                word_type=''
            if pronounciation:
                pronounciation = ' [' + pronounciation + ']'
            if meaning:
                meaning =  '   \"' + meaning + '\"'

            f2.write('{word}  {sl_word}{pronounciation}{meaning}\n'.format(word=word,  sl_word=sl_word, meaning=meaning, pronounciation=pronounciation))
        f2.close()


    def se(self, quit_sig=False):
        ' short for save exit, actually it is often used for backup'
        f = open('Dict_backup.py', 'a')
        now = str(datetime.datetime.now())[:19]
        saving_data = pickle.dumps(self)
        f.write('\nlast_time=%r\n' % now)
        f.write('sig=%s_%s_dict\n' % (self.first_lan, self.second_lan))
        f.write('data=%r\n' % saving_data)
        f.close()
        if quit_sig:
            sys.exit(0)

    def exam(self, rev=True, L2=False, T=False, target = [], st=False, brief=False):
        """Default to rank from the word you forgot the most times, pass any value to rank from reverse
        L2 = bilingual, rev = Reverse, T = by time order, st = test Sentence, you can use v() to pass a filtered target list to exam(), brief meanse only examing words with forget_score >= 0
        考试的时候有一个机制，对于遗忘积分为负(已记忆)的单词选取不频繁，但如果抽到的标记为已记忆的单词如果忘记的话，就增大抽查频率，直到100%, 如果抽查已记忆单词全部回答正确，就减少抽查比例，最低减到2%, 那么记住1万个单词考试一次最少是200个单词， 初始值是30%。
        """

        # sentence test begin

        if st:
            agent = self.show_st(exam=True)
            for index, sentence in agent:
                print sentence, '\n'
                answer = raw_input('You remember this sentence?')
                if answer in ['y', 'yes', 's', 'si']:
                    self.st_dict[index]['forget_score'] -= 1
                    self.add_score(1)
                else:
                    self.st_dict[index]['forget_score'] += 1
                    self.add_score(-2)
            self.save()
            return

        # sentence test end

        target = target or [ word for word in sorted(self.raw_dict.keys(), key=lambda x: self.raw_dict[x].get('create_time', datetime.datetime(2006, 07, 11, 21, 13, 29, 296140)) if T else self.raw_dict[x].get('forget_score') , reverse = rev)  if self.raw_dict[word]['forget_score'] >= 0 ]

        Errors = []

        # M_sample means memorized word sample
        Memorized_words = [ word for word in self.raw_dict.keys() if self.raw_dict[word].get('forget_score', 0) < 0 ]
        sample_num =  int(round((len(Memorized_words) * self.exam_rate) / 100))
        for i in xrange(sample_num):
            M_sample = random.sample(Memorized_words, sample_num)


        for word in target:
            if self.raw_dict[word]['forget_score'] < 0:
                M_sample.append(word)

        for i in target:

            if brief:
                if self.raw_dict[i].get('forget_score', 0) < 0:
                    continue

            if L2:
                if not self.raw_dict[i].get('sl_word'):
                    continue

                else:
                    print '\n'
                    print 'Please type the Spanish/English version of: ', i
                    answer = raw_input('>>>')

                    if answer == self.raw_dict[i]['sl_word']:
                        self.raw_dict[i]['forget_score'] -= 1
                        self.add_score(1)
                        print '\n'
                        self.g(old_word=i)
                    else:
                        self.raw_dict[i]['forget_score'] += 1
                        self.add_score(-2)
                        Errors.append(i)
                        print '\n'
                        self.g(old_word=i)
                        print '\n'

            else:
                print '\n'
                print 'Do you remember: ', i, '?'
                answer = raw_input('type y for yes, and others for no: ')

                if answer == 'y' or answer == 'yes':
                    self.raw_dict[i]['forget_score'] -= 1
                    self.add_score(1)
                    print '\n'
                    self.g(old_word=i)
                else:
                    self.raw_dict[i]['forget_score'] += 1
                    self.add_score(-2)
                    Errors.append(i)
                    print '\n'
                    self.g(old_word=i)

        if Errors:
            print 'These are the words you failed in this exam, you can put more effort on them later.\n'
            for i in Errors:
                print '\t\t', i
            M_errors_num =  len(set(Errors) & set(M_sample))
            if M_errors_num:
                extra_exam_rate = int(round(M_errors_num)*100/len(M_sample))
                self.exam_rate += extra_exam_rate
                if self.exam_rate > 100:
                    self.exam_rate = 100

        else:
            if self.exam_rate >= 4 and M_sample:
                self.exam_rate -= 2

        self.save()

    def get_current_category(self):
        L = []
        for i in self.raw_dict:
            category = self.raw_dict[i].get('category')
            if category:
                if type(category) == list:
                    L.extend(self.raw_dict[i]['category'])
                elif type(category) == str:
                    L.append(self.raw_dict[i]['category'])

        S = set(L)

        return ("\t").join([i for i in S])

    def c(self):
        """ Short for category """
        old_word = raw_input('Enter the word:')

        if old_word in self.raw_dict:
            if self.raw_dict[old_word].get('category'):
                print 'Current categories for this word:', '\t'.join(self.raw_dict[old_word]['category']), '. Type y to add new category, type others to quit'
                choice = raw_input('>>>')
                if choice not in ['y', 'yes']:
                    return
                else:
                    current_category = self.get_current_category()
                    print "Current exists categories are: ", current_category
                    category =  raw_input("Enter your category below and press ENTER when finished typing:\n\n")
                    if not category in self.raw_dict[old_word]['category']:
                        self.raw_dict[old_word].setdefault['category'] = category
                    self.add_score(0.5)
            else:
                self.raw_dict[old_word]['category'] = []
                current_category = self.get_current_category()
                print "Current exists categories are: ", current_category
                category =  raw_input("Enter your category below and press ENTER when finished typing:\n\n")
                self.raw_dict[old_word].setdefault['category'] = [category]
                self.add_score(0.5)
        else:
            print " The word you are searching for is not in this dict now, please check your spelling."

        self.save()

    def vc(self):
        """ short for view category """
        result =  self.get_current_category()
        return result

    def add_score(self, num=1):
        self.score += num

    def x(self):
        'x is short for experience'
        print "YOUR SCORE: ", self.score

    def show_init_score(self):   # single-use function, obsolete now
        temp_score = 0
        for word in self.raw_dict:
            for item in self.raw_dict[word]:
                if self.raw_dict[word][item]:
                    temp_score += 1
        print temp_score

    def init_exam(self):
        forget_word_num = 0
        unmemorized_word_num = 0
        for i in self.raw_dict:
            forget_score = self.raw_dict[i].get('forget_score', 0)
            if forget_score >= 1:
                forget_word_num += 1
            if forget_score == 0:
                unmemorized_word_num += 1
        if forget_word_num > 15 or unmemorized_word_num > 20:
            print "\n\n\n\n\n YOU HAVE %d FORGOTTEN WORDS AND %d UNMEMORIZED WORDS, PLEASE DO THE EXAM RIGHT NOW. \n\n\n\n\n" % (forget_word_num, unmemorized_word_num)

            choice = raw_input("Do the exam right now?")

            if choice in ['y', 'yes', 'sí', 'OK', 'vale', 'fine']:
                self.exam()

        else:
            pass
    #        print "\nANYWAY, BUDDY, YOU CAN'T ESCAPE OF THIS EXAM, NOW TAKE IT!"
    #        exam()

    def st(self, d=False):
        """ short for sentence, d = delete signal """
        used_index = set(self.st_dict.keys())
        index_pool = set(range(100000))
        usable_index = index_pool - used_index
        if not usable_index:
            print " You have reached the limit of sentence dict: 100000, so no more sentence could be add. "
            return
        else:
            next_index = sorted(list(usable_index))[0]

        sentence = raw_input('please type the sentence below:\n\n')

        exist_sentence = set([x['sentence'] for x in self.st_dict.values()])

        if sentence not in exist_sentence:
            self.st_dict[next_index] = {'forget_score': 0, 'sentence': sentence}
        else:
            print " This sentence is already in sentence dict "
            return

        self.save()

    def show_st(self, exam=False):

        temp = []
        for index in sorted(self.st_dict.keys(), key=lambda x: self.st_dict[x]['forget_score']):
            sentence = self.st_dict[index]['sentence']

            if not exam:
                print 'index: ', index,'\n'
                print sentence, '\n\n'

            else:
                temp.append((index, sentence))

        if exam:
            return temp

if sig == 's':
    get_dict('Spanish', 'English')
elif sig == 'e':
    get_dict('English', 'Spanish')
else:
    get_dict()

