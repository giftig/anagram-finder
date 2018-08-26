#!/usr/bin/env python2.7

import re
import os
import sys


def main():
    tiles = sorted(sys.argv[1].upper().replace('?', '.'))
    pattern = '^%s%s$' % (
        ''.join(tiles[:2]),
        ''.join([t + '?' for t in tiles[2:]])
    )
    pattern = re.compile(pattern)
    dictfile = os.path.join(os.path.dirname(sys.argv[0]), 'scrabble-words.txt')

    words = []

    with open(dictfile, 'rb') as f:
        words = [
            l.strip() for l in f
        ]

    words = [(w, ''.join(sorted(w))) for w in words]

    matches = [w for (w, canon) in words if pattern.match(canon)]
    matches = sorted(matches, key = lambda m: (-len(m), m))
    for m in matches:
        print m


if __name__ == '__main__':
    main()
