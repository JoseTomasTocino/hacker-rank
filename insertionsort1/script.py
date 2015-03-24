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
    pl = lambda l, s: s.join(str(x) for x in l)

    array_size = int(sys.stdin.readline())
    the_array = [int(x) for x in sys.stdin.readline().strip().split()]

    element = the_array[-1]
    current_index = array_size - 2

    while (True):

        if current_index == -1 or the_array[current_index] <= element:
            the_array[current_index + 1] = element
            break
        else:
            the_array[current_index + 1] = the_array[current_index]
            current_index -= 1

        print pl(the_array, " ")

    print pl(the_array, " ")

if __name__ == '__main__':
    main()

