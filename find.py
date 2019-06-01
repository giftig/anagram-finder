#!/usr/bin/env python2.7

import os
import sys


def get_words():
    dictfile = os.path.join(os.path.dirname(sys.argv[0]), 'scrabble-words.txt')
    with open(dictfile, 'rb') as f:
        return [l.strip() for l in f]


def _pretty_results(solutions):
    by_len = {}
    for s in solutions:
        sol_len = len(s)
        entry = by_len.get(sol_len, [])
        entry.append(s)
        by_len[sol_len] = entry

    by_len = sorted(by_len.items(), key=lambda k: -k[0])
    for result_len, results in by_len:
        print '%d-letter words:' % result_len
        print '   '.join([r for r in results])
        print ''


def display_results(solutions):
    if sys.stdout.isatty():
        return _pretty_results(solutions)

    for s in sorted(solutions, key=lambda s: (len(s), s)):
        print s


def main(phrase):
    tiles = sorted(phrase.upper().replace('.', '?'))
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

    display_results(solutions)


if __name__ == '__main__':
    main(sys.argv[1])
