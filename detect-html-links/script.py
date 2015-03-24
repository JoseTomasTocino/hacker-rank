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

def get_tag_content(tag, fetch_attributes = True):
    tag = tag.strip()

    if not tag:
        return ""
    elif tag[0] != "<":
        return tag

    # Get the tag name
    tag_match = re.match(r"""<([a-z]+)""", tag)
    tag_name = tag_match.group(1)

    if tag_name == "img":
        return ""

    # Get the entire opening tag
    tag_match = re.match(r"""<([a-z]+)(?:\s+[a-z]+="[^"]*")*>""", tag)
    opening_tag = tag_match.group(0)
    content_start = len(opening_tag)

    # Get the tag attributes
    tag_attributes = {x.group(1): x.group(2) for x in re.finditer(r"""([a-z]+)="([^"]*)""", opening_tag)}

    # Find the closing tag position
    content_end = tag.rfind("</{}>".format(tag_name))

    # Get the tag content
    content = tag[content_start:content_end]

    subcontent = get_tag_content(content, fetch_attributes=False)

    if fetch_attributes:
        return (subcontent, tag_attributes)
    else:
        return subcontent

def main():
    numCases = sys.stdin.readline()
    text = "".join((x.strip() for x in sys.stdin.readlines()))

    link_start = 0
    link_end = 0
    current_index = 0

    links = []

    while True:
        try:
            link_start = text.index("<a ", link_start)
            link_end = text.index("</a>", link_start)

            links.append((link_start, link_end))
            link_start = link_end + 4

        except:
            break

    for pair in links:
        tag = text[pair[0]:pair[1] + 4]
        tag_text, tag_attributes = get_tag_content(tag)
        print "{},{}".format(tag_attributes['href'].strip(), tag_text.strip())

if __name__ == '__main__':
    main()

