import sys
import os
import textwrap

# https://adventofcode.com/2025/day/4

def partOne():
  rolls = parseInput()
  locs = []
  row = len(rolls)
  col = len(rolls[0])
  for i in range(row):
    for j in range(col):
      if rolls[i][j] == '@':
        locs.append((i, j))
  rolls, rem_locs = remove(rolls, locs, row, col)
  print(len(locs) - len(rem_locs))

def remove(rolls, locs, row, col):
  dirs = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
  rem_locs = []
  removed = []
  for loc in locs:
    i, j = loc
    adj_count = 0
    for dir in dirs:
      ii = i + dir[0]
      jj = j + dir[1]
      if ii >= 0 and jj >= 0 and ii < row and jj < col and rolls[ii][jj] == '@':
        adj_count += 1
    if adj_count >= 4:
      rem_locs.append((i, j))
    else:
      removed.append((i, j))
  
  for loc in removed:
    rolls[loc[0]][loc[1]] = '.'
  
  return rolls, rem_locs

def partTwo():
  rolls = parseInput()
  locs = []
  row = len(rolls)
  col = len(rolls[0])
  for i in range(row):
    for j in range(col):
      if rolls[i][j] == '@':
        locs.append((i, j))
  original = locs
  while True:
    rolls, rem_locs = remove(rolls, locs, row, col)
    if len(rem_locs) == len(locs):
      break
    locs = rem_locs
  print(len(original) - len(locs))

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))  
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
