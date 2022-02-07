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
    currentwordletters = []
    for letter in word:
        if letter == 'a':
            if letter in currentwordletters:
                wordscore += (aratio / 3)
            else:
                wordscore += aratio
            currentwordletters.append(letter)
        if letter == 'b':
            if letter in currentwordletters:
                wordscore += (bratio / 3)
            else:
                wordscore += bratio
            currentwordletters.append(letter)
        if letter == 'c':
            if letter in currentwordletters:
                wordscore += (cratio / 3)
            else:
                wordscore += cratio
            currentwordletters.append(letter)
        if letter == 'd':
            if letter in currentwordletters:
                wordscore += (dratio / 3)
            else:
                wordscore += dratio
            currentwordletters.append(letter)
        if letter == 'e':
            if letter in currentwordletters:
                wordscore += (eratio / 3)
            else:
                wordscore += eratio
            currentwordletters.append(letter)
        if letter == 'f':
            if letter in currentwordletters:
                wordscore += (fratio / 3)
            else:
                wordscore += fratio
            currentwordletters.append(letter)
        if letter == 'g':
            if letter in currentwordletters:
                wordscore += (gratio / 3)
            else:
                wordscore += gratio
            currentwordletters.append(letter)
        if letter == 'h':
            if letter in currentwordletters:
                wordscore += (hratio / 3)
            else:
                wordscore += hratio
            currentwordletters.append(letter)
        if letter == 'i':
            if letter in currentwordletters:
                wordscore += (iratio / 3)
            else:
                wordscore += iratio
            currentwordletters.append(letter)
        if letter == 'j':
            if letter in currentwordletters:
                wordscore += (jratio / 3)
            else:
                wordscore += jratio
            currentwordletters.append(letter)
        if letter == 'k':
            if letter in currentwordletters:
                wordscore += (kratio / 3)
            else:
                wordscore += kratio
            currentwordletters.append(letter)
        if letter == 'l':
            if letter in currentwordletters:
                wordscore += (lratio / 3)
            else:
                wordscore += lratio
            currentwordletters.append(letter)
        if letter == 'm':
            if letter in currentwordletters:
                wordscore += (mratio / 3)
            else:
                wordscore += mratio
            currentwordletters.append(letter)
        if letter == 'n':
            if letter in currentwordletters:
                wordscore += (nratio / 3)
            else:
                wordscore += nratio
            currentwordletters.append(letter)
        if letter == 'o':
            if letter in currentwordletters:
                wordscore += (oratio / 3)
            else:
                wordscore += oratio
            currentwordletters.append(letter)
        if letter == 'p':
            if letter in currentwordletters:
                wordscore += (pratio / 3)
            else:
                wordscore += pratio
            currentwordletters.append(letter)
        if letter == 'q':
            if letter in currentwordletters:
                wordscore += (qratio / 3)
            else:
                wordscore += qratio
            currentwordletters.append(letter)
        if letter == 'r':
            if letter in currentwordletters:
                wordscore += (rratio / 3)
            else:
                wordscore += rratio
            currentwordletters.append(letter)
        if letter == 's':
            if letter in currentwordletters:
                wordscore += (sratio / 3)
            else:
                wordscore += sratio
            currentwordletters.append(letter)
        if letter == 't':
            if letter in currentwordletters:
                wordscore += (tratio / 3)
            else:
                wordscore += tratio
            currentwordletters.append(letter)
        if letter == 'u':
            if letter in currentwordletters:
                wordscore += (uratio / 3)
            else:
                wordscore += uratio
            currentwordletters.append(letter)
        if letter == 'v':
            if letter in currentwordletters:
                wordscore += (vratio / 3)
            else:
                wordscore += vratio
            currentwordletters.append(letter)
        if letter == 'w':
            if letter in currentwordletters:
                wordscore += (wratio / 3)
            else:
                wordscore += wratio
            currentwordletters.append(letter)
        if letter == 'x':
            if letter in currentwordletters:
                wordscore += (xratio / 3)
            else:
                wordscore += xratio
            currentwordletters.append(letter)
        if letter == 'y':
            if letter in currentwordletters:
                wordscore += (yratio / 3)
            else:
                wordscore += yratio
            currentwordletters.append(letter)
        if letter == 'z':
            if letter in currentwordletters:
                wordscore += (zratio / 3)
            else:
                wordscore += zratio
            currentwordletters.append(letter)
    word_scores[word] = wordscore
f = open("sortedwordlist.txt", "a")
sorted_word_scores = dict( sorted(word_scores.items(), key=operator.itemgetter(1),reverse=True))
print(str(sorted_word_scores))
for key in sorted_word_scores:
    f.write(key + '\n')
f.close()