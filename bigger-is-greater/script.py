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

def main():
    numCases = int(sys.stdin.readline())

    for case in sys.stdin:
        case = list(case.strip())
        original_case = case[:]
        caselen = len(case)

        # If the word has only one letter, it's not possible
        if len(set(case)) == 1:
            print "no answer"
            continue

        pivot_letter = case[-1]
        pivot_letter_index = len(case) - 1

        for i, current_letter in enumerate(case[-2::-1]):
            real_i = caselen - (i + 2)

            if pivot_letter > current_letter:
                case[real_i], case[pivot_letter_index] = case[pivot_letter_index], case[real_i]
                case[real_i + 1:] = sorted(case[real_i + 1:])
                break

            elif current_letter == pivot_letter:
                case[real_i + 1:] = sorted(case[real_i + 1:])
                break

        if case == original_case:
            print "no answer"
        else:
            print ''.join(case)


if __name__ == '__main__':
    main()

