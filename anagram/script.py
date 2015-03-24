#!/usr/bin/env python
# All I want to do is coding: utf-8

# Copyright (C) 2015 José Tomás Tocino García <theom3ga@gmail.com>

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

import sys, re
from collections import Counter

def main():
    numCases = int(sys.stdin.readline().strip())

    for case in sys.stdin:
        case = case.strip()

        strlen = len(case)

        if strlen % 2 != 0:
            print -1
            continue

        s1, s2 = case[0:strlen/2], case[strlen/2:]

        c1 = Counter(s1)
        c2 = Counter(s2)

        print sum((c1-c2).values())

if __name__ == '__main__':
    main()

