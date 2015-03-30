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
import heapq
from collections import deque

def main():
    num_cases = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    h = []

    for case in sys.stdin:
        heapq.heappush(h, int(case.strip()))

    min_unfairness = None

    # Store first K elements
    elems = deque()
    [elems.append(heapq.heappop(h)) for x in range(K - 1)]

    while h:
        # Get next element (max)
        next_element = heapq.heappop(h)

        # Get current element (min)
        current_element = elems.popleft()

        # Compute the fairness
        current_unfairness = next_element - current_element

        # Keep track of the minimum fairness
        if not min_unfairness or min_unfairness > current_unfairness:
            min_unfairness = current_unfairness

        # Append the next element to the current elements container
        elems.append(next_element)

    print min_unfairness

if __name__ == '__main__':
    main()

