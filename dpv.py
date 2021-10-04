#!/bin/python

import sys


h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()
hi = 0
for c in word:
    hi = max(hi, h[ord(c)-ord('a')])
print hi * len(word)
