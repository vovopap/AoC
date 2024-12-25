import sys
import os

# https://adventofcode.com/2024/day/25

def partOne():
  locks, keys = parseInput()
  res = 0
  for lock in locks:
    for key in keys:
      overlap = False
      for i in range(5):
        if lock[i] + key[i] > 7:
          overlap = True
          break
      if not overlap:
        res += 1
  print(res)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  schemes = [[list(line) for line in scheme.splitlines()] for scheme in open(f'{dir_path}/input.txt', 'r').read().split('\n\n')]
  locks = []
  keys = []
  for scheme in schemes:
    combo = [0, 0, 0, 0, 0]
    for i in range(7):
      for j in range(5):
        if scheme[i][j] == '#':
          combo[j] += 1
    if is_lock(scheme[6]):
      locks.append(combo)
    else:
      keys.append(combo)
  return locks, keys

def is_lock(line):
  return line[0] == '.' and line[1] == '.' and line[2] == '.' and line[3] == '.' and line[4] == '.'

if sys.argv[1] == 'one':
  partOne()