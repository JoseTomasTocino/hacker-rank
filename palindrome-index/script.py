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
from itertools import izip

logger = logging.getLogger("myLogger")

def is_palindrome (s):
    for c1, c2 in izip(s, reversed(s)):
        if c1 != c2:
            return False
    return True

def main():
    numCases = int(sys.stdin.readline())

    results = []

    for case in sys.stdin:
        case = case.strip()

        if is_palindrome(case):
            results.append(-1)
            continue

        else:
            # Optimization: check common characters to skip a good chunk
            advance = 0
            for c1, c2 in izip(case, reversed(case)):
                if c1 != c2:
                    break
                advance += 1

            substring = case[advance:len(case) - advance]

            for i in range(len(substring)):
                if is_palindrome(substring[0:i] + substring[i+1:]):
                    results.append(advance + i)
                    break

    for res in results:
        print res


if __name__ == '__main__':
    main()

