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
from collections import defaultdict

def check_subtree(tree, node, visited_nodes, edges_to_cut):
    result = 0
    visited_nodes.add(node)

    # Only connection is the parent node
    if len(tree[node]) == 1:
        return 1

    # Basically, count the children of the current node. If that, plus 1 (the
    # current node) is even, then they can form a correct subtree, so update the
    # number of edges to cut
    else:
        s = [check_subtree(tree, x, visited_nodes, edges_to_cut) for x in tree[node] if x not in visited_nodes]
        ss = sum(s) + 1
        if ss % 2 == 0:
            edges_to_cut[0] += 1

        return sum(s) + 1

def main():
    n_vertices, n_edges = [int(x) for x in sys.stdin.readline().strip().split()]
    tree = defaultdict(dict)

    visited_nodes = set()

    for edge in sys.stdin:
        ui, vi = [int(x) for x in edge.strip().split()]

        tree[ui][vi] = True
        tree[vi][ui] = True

    edges_to_cut = [0]
    check_subtree(tree, 1, visited_nodes, edges_to_cut)

    print edges_to_cut[0] - 1

if __name__ == '__main__':
    main()

