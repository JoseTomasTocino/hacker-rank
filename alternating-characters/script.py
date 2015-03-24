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

from itertools import groupby

def main():
    numCases = int(sys.stdin.readline())

    for case in sys.stdin:
        case = case.strip()

        # Essentially, group the consecutive elements in groups of the same character,
        # get the amount of repeated characters for each group (that's the length minus one),
        # and sum that amount for all the groups
        print sum([len(x) - 1 for x in [list(g) for k, g in groupby(case)]])

if __name__ == '__main__':
    main()
