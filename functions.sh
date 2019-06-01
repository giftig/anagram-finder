#!/bin/bash

DIR=$(dirname $0)

_scrabble_anagram() {
  "$HOME/code/tiny/anagram-finder/find.py" "$@"
}

_scrabble_like() {
  grep -i -E "$1" "$HOME/code/tiny/anagram-finder/scrabble-words.txt"
}

scrabble() {
  case "$1" in
    anagram)
      shift
      _scrabble_anagram "$@"
      ;;
    around|one|1)
      shift
      _scrabble_like '^.'"$1"'$'
      _scrabble_like '^'"$1"'.$'
      ;;
    like)
      shift
      _scrabble_like "$@"
      ;;
    exact|match|check)
      shift
      _scrabble_like "^$1"'$'
      ;;
    *)
      _scrabble_anagram "$@"
      ;;
  esac
}
