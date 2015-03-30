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
import math

def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]

    mean = 0.0

    # On each step, compute the variation in the mean, which is
    # (number of affected jars * increase) / total jars

    for case in sys.stdin:
        a, b, k = [int(x) for x in case.strip().split()]

        mean += ((b - a + 1) * k) / float(N)

    print int(mean)

if __name__ == '__main__':
    main()

