#!/bin/bash

_scrabble_anagram() {
  "$HOME/Code/tiny/anagram-finder/find.py" "$@"
}

_scrabble_like() {
  grep -i -E "$1" "$HOME/Code/tiny/anagram-finder/scrabble-words.txt"
}

scrabble() {
  case "$1" in
    anagram)
      shift
      _scrabble_anagram "$@"
      ;;
    like)
      shift
      _scrabble_like "$@"
      ;;
    *)
      _scrabble_anagram "$@"
      ;;
  esac
}
