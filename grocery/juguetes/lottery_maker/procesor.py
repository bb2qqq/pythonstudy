f = open('dbl_num_data', 'r')
great_dict = {}
blue_dict = {}
for i in f:
    i = i.rstrip('\n')
    i = i.split()
    blue = i.pop(-1)

    if blue in blue_dict:
        blue_dict[blue] += 1
    else:
        blue_dict[blue] = 1

    for n in i:
        if n in great_dict:
            great_dict[n] += 1
        else:
            great_dict[n] = 1

print 'normal'
for n in sorted(great_dict.keys(), key = lambda x: great_dict[x], reverse = True):
    print n, great_dict[n]
print 'total_num', len(great_dict)

print '\n\n', 'Blue'
for n in sorted(blue_dict.keys(), key = lambda x: blue_dict[x], reverse = True):
    print n, blue_dict[n]
print 'total_num', len(blue_dict)

great_list = []
blue_list = []
