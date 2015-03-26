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
from operator import xor
from collections import defaultdict

def xor_reduce(B, start, end, S):

    if start not in xor_reduce.memory:
        xor_reduce.memory[start][end] = reduce(xor, B[start:end])

    elif end not in xor_reduce.memory[start]:
        max_processed_index = max(xor_reduce.memory[start].keys())
        max_processed = xor_reduce.memory[start][max_processed_index]
        xor_reduce.memory[start][end] = reduce(xor, [max_processed] + B[max_processed_index + 1:end])

    return xor_reduce.memory[start][end] ^ S

xor_reduce.memory = defaultdict(dict)

def main():
    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    S = [int(x) for x in sys.stdin.readline().strip()]
    B = [0] * N

    # Base case, B[0] = S[0]
    B[0] = S[0]

    for i in xrange(1, N):
        if i < K:
            B[i] = xor_reduce(B, 0, i, S[i])
            # B[i] = reduce(xor, B[:i]) ^ S[i]
        else:
            B[i] = xor_reduce(B, i - K + 1, i, S[i])
            # B[i] = reduce(xor, B[i - K + 1:i]) ^ S[i]

    print "".join(str(x) for x in B)

if __name__ == '__main__':
    main()

