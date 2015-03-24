#!/usr/bin/env python
# All I want to do is coding: utf-8

# Copyright (C) 2014 José Tomás Tocino García <theom3ga@gmail.com>

# Autor: José Tomás Tocino García

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import sys
import logging
from operator import itemgetter

# logging.basicConfig(level=logging.DEBUG)

def reduce_word (word, letters):
    return ''.join([x for x in word if x in letters])

def longest(l):
    if not l:
        return None

    return sorted(((x, len(x)) for x in l), key=itemgetter(1), reverse=True)[0][0]

def LCS(S, T):
    m = len(S)
    n = len(T)
    L = [[0] * (n+1) for i in range(m+1)]
    LCS_set = set()
    longest = 0

    for i in xrange(m):
        for j in xrange(n):
            if S[i] == T[j]:
                v = L[i][j] + 1
                L[i+1][j+1] = v

                if v > longest:
                    longest = v
                    LCS_set = set()

                if v == longest:
                    LCS_set.add(S[i-v+1:i+1])

    return LCS_set

def main():
    w1 = sys.stdin.readline().strip()
    w2 = sys.stdin.readline().strip()

    logging.info("W1: %s", w1)
    logging.info("W2: %s", w2)

    common_letters = set.intersection(*[set(x) for x in [w1, w2]])

    logging.info("Common letters: %s", common_letters)

    rw1 = reduce_word(w1, common_letters)
    rw2 = reduce_word(w2, common_letters)

    logging.info("RW1: %s", rw1)
    logging.info("RW2: %s", rw2)

    next1 = {}
    for i,c in enumerate(rw1):
        if c not in next1:
            next1[c] = rw1[i+1:]

    next2 = {}
    for i,c in enumerate(rw2):
        if c not in next2:
            next2[c] = rw2[i+1:]

    logging.info("Next1: %s", next1)
    logging.info("Next2: %s", next2)

    comm = {x: longest(LCS(next1[x], next2[x])) for x in common_letters}

    logging.info("Common: %s", comm)
    joined = [len(x+comm[x]) for x in comm if comm[x] ]
    joined.append(0)

    print max(joined)

if __name__ == '__main__':
    main()

