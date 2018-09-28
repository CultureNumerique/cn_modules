#!/usr/bin/env python

"""
Pandoc filter to convert all level 2+ headers to paragraphs with
emphasized text.
"""

from pandocfilters import toJSONFilter, Para


def behead(key, value, format, meta):
    if key == 'CodeBlock':
        return Para([])


if __name__ == "__main__":
    toJSONFilter(behead)
