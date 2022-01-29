#!/usr/bin/env python3
import operator

with open('possibleanswerswordlist.txt', 'r') as f:
    words = [line.rstrip() for line in f.readlines()]
all_freq = {}
count = 0

for word in words:
    for letter in word:
        count += 1
        if letter in all_freq:
            all_freq[letter] += 1
        else:
            all_freq[letter] = 1

aratio = all_freq['a'] / count * 100
bratio = all_freq['b'] / count * 100
cratio = all_freq['c'] / count * 100
dratio = all_freq['d'] / count * 100
eratio = all_freq['e'] / count * 100
fratio = all_freq['f'] / count * 100
gratio = all_freq['g'] / count * 100
hratio = all_freq['h'] / count * 100
iratio = all_freq['i'] / count * 100
jratio = all_freq['j'] / count * 100
kratio = all_freq['k'] / count * 100
lratio = all_freq['l'] / count * 100
mratio = all_freq['m'] / count * 100
nratio = all_freq['n'] / count * 100
oratio = all_freq['o'] / count * 100
pratio = all_freq['p'] / count * 100
qratio = all_freq['q'] / count * 100
rratio = all_freq['r'] / count * 100
sratio = all_freq['s'] / count * 100
tratio = all_freq['t'] / count * 100
uratio = all_freq['u'] / count * 100
vratio = all_freq['v'] / count * 100
wratio = all_freq['w'] / count * 100
xratio = all_freq['x'] / count * 100
yratio = all_freq['y'] / count * 100
zratio = all_freq['z'] / count * 100

word_scores = {}
for word in words:
    wordscore = 0
    for letter in word:
        if letter == 'a':
            wordscore += aratio
        if letter == 'b':
            wordscore += bratio
        if letter == 'c':
            wordscore += cratio
        if letter == 'd':
            wordscore += dratio
        if letter == 'e':
            wordscore += eratio
        if letter == 'f':
            wordscore += fratio
        if letter == 'g':
            wordscore += gratio
        if letter == 'h':
            wordscore += hratio
        if letter == 'i':
            wordscore += iratio
        if letter == 'j':
            wordscore += jratio
        if letter == 'k':
            wordscore += kratio
        if letter == 'l':
            wordscore += lratio
        if letter == 'm':
            wordscore += mratio
        if letter == 'n':
            wordscore += nratio
        if letter == 'o':
            wordscore += oratio
        if letter == 'p':
            wordscore += pratio
        if letter == 'q':
            wordscore += qratio
        if letter == 'r':
            wordscore += rratio
        if letter == 's':
            wordscore += sratio
        if letter == 't':
            wordscore += tratio
        if letter == 'u':
            wordscore += uratio
        if letter == 'v':
            wordscore += vratio
        if letter == 'w':
            wordscore += wratio
        if letter == 'x':
            wordscore += xratio
        if letter == 'y':
            wordscore += yratio
        if letter == 'z':
            wordscore += zratio
    word_scores[word] = wordscore
f = open("sortedwordlist.txt", "a")
sorted_word_scores = dict( sorted(word_scores.items(), key=operator.itemgetter(1),reverse=True))
print(str(sorted_word_scores))
for key in sorted_word_scores:
    f.write(key + '\n')
f.close()