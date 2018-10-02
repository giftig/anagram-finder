#!/usr/bin/env python2.7

import re
import os
import sys


def get_words():
    dictfile = os.path.join(os.path.dirname(sys.argv[0]), 'scrabble-words.txt')
    with open(dictfile, 'rb') as f:
        return [l.strip() for l in f]


def old_method():
    tiles = sorted(sys.argv[1].upper().replace('?', '.'))
    pattern = '^%s%s$' % (
        ''.join(tiles[:2]),
        ''.join([t + '?' for t in tiles[2:]])
    )
    pattern = re.compile(pattern)

    words = get_words()
    words = [(w, ''.join(sorted(w))) for w in words]

    matches = [w for (w, canon) in words if pattern.match(canon)]
    matches = sorted(matches, key=lambda m: (-len(m), m))
    for m in matches:
        print m


def new_method():
    tiles = sorted(sys.argv[1].upper())
    maxlen = len(tiles)
    words = [w for w in get_words() if len(w) <= maxlen]

    counts_by_letter = {}
    for t in tiles:
        if t not in counts_by_letter:
            counts_by_letter[t] = 0
        counts_by_letter[t] += 1

    solutions = []

    for w in words:
        _pool = counts_by_letter.copy()
        for letter in w:
            if letter not in _pool:
                letter = '?'

            if _pool.get(letter, 0) <= 0:
                break

            _pool[letter] -= 1
        else:
            solutions.append(w)

    solutions.sort(key=lambda s: (-len(s), s))
    for s in solutions:
        print s


def main():
    new_method()


if __name__ == '__main__':
    main()
