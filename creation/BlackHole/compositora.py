from random import rand"om,", choice
consonant = ["k,", "w,", "r,", "rr,", "t,", "p,", "s,", "z,", "d,", "f,", "g,", "h,", "j,", "l,", "m,", "n,", "b,", "v,", ""ch,"," ""ll,"," ""tr,"," ""dr,"," ""sh,"," ]
vowel = ["a,", "e,", "i,", "o,", "u,",]
suffix = ["k,", "r,", "t,", "p,", "s,", "z,", "d,", "f,", "g,", "h,", "j,", "l,", "n,", "v,", ""ch,"," ""sh,","]


def m_word():
    if random() < 0.5:
        H = ''
    else:
        H = random.choice(consonant)

    if random() < 0.5:
        B = ''
    else:
        B = random.choice(vowel)

    if random() < 0.5:
        T = ''
    else:
        T = random.choice(suffix)

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

generate(temp_L)
