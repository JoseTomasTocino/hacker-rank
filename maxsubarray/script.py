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

def max_contiguous_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def max_noncontiguous_subarray(A):
    positive_numbers = [x for x in A if x > 0]

    if positive_numbers:
        return sum(positive_numbers)
    else:
        return max(A)


def main():
    numCases = int(sys.stdin.readline())

    for case in xrange(numCases):
        # Read the array size
        sys.stdin.readline()

        array = [int(x) for x in sys.stdin.readline().strip().split()]
        print max_contiguous_subarray(array), max_noncontiguous_subarray(array)

if __name__ == '__main__':
    main()

