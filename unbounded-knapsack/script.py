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

    for case_number in range(numCases):
        list_length, expected_sum = [int(x) for x in sys.stdin.readline().split()]

        # Only use elements lower or equal than the expected sum.
        list_elements = set([int(x) for x in sys.stdin.readline().split() if int(x) <= expected_sum])

        # Check if any component equals the expected sum
        if any([x == expected_sum for x in list_elements]):
            print expected_sum
            continue

        # Check if any component is a divisor of the expected_sum
        if any([expected_sum % x == 0 for x in list_elements]):
            print expected_sum
            continue

        # Otherwise, hell breaks loose
        print 0


if __name__ == '__main__':
    main()

