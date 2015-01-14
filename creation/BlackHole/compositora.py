from random import random, choice
consonant = ['k', 'w', 'r', 'rr', 't', 'p', 's', 'z', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'b', 'v', 'ch', 'll', 'tr', 'dr', 'sh', ]
vowel = ['a', 'e', 'i', 'o', 'u',]
vowel_compound = [ 'an', 'en', 'in', 'on', 'un', 'ang', 'eng', 'ing', 'ong', 'ung', 'uai', 'ae', 'ai', 'ao', 'au', 'ea', 'ei', 'eo', 'eu', 'ia', 'ie', 'io', 'iu', 'oa', 'oe', 'oi', 'ou', 'ua', 'ue', 'ui', 'uo']
suffix = ['k', 'r', 't', 'p', 's', 'z', 'd', 'f', 'g', 'h', 'j', 'l', 'n', 'v', 'ch', 'sh',]


def m_word(h_rate=0.2, b_rate=0.2, t_rate=0.8):
    compound_sig = False
    if random() < h_rate:
        H = ''
    else:
        H = choice(consonant)

    if random() < b_rate:
        B = choice(vowel_compound)
        compound_sig = True
    else:
        B = choice(vowel)

    if not compound_sig:
        if random() < t_rate:
            T = ''
        else:
            T = choice(suffix)

    else:
        T = ''

    word = H + B + T
    return word

def generate(L):
    for serie_number in L:
        temp_L = []
        for x in xrange(serie_number):
            word = m_word()
            temp_L.append(word)
        temp_L = ' '.join(temp_L)
        print temp_L



test_L = [7, 8, 8, 8, 3, 3, 8, 3, 3, 7]

generate(test_L)
