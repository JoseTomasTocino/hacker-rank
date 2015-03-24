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


def main():
    numSentences = int(sys.stdin.readline().strip())
    sentences = [sys.stdin.readline().strip() for x in range(numSentences)]

    numWords = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for x in range(numWords)]

    for word in words:
        acum = 0
        for sentence in sentences:
            res = re.findall(r"""\b""" + word + r"""\b""", sentence)
            acum += len(res)

        print acum

if __name__ == '__main__':
    main()
