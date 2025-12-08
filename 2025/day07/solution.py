import sys
import os

# https://adventofcode.com/2025/day/7

def partOne():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  locs = set()
  splits = set()
  for j in range(col):
    if grid[0][j] == 'S':
      locs.add(j)
  for i in range(1, row):
    new_locs = set()
    for loc in locs:
      if grid[i][loc] == '.':
        new_locs.add(loc)
      else:
        splits.add((i, loc))
        new_locs.add(loc - 1)
        new_locs.add(loc + 1)
    locs = new_locs
  print(len(splits))

def partTwo():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  mem = {}
  for j in range(col):
    if grid[0][j] == 'S':
      print(backtrack(1, j, row, col, grid, mem))

def backtrack(i, j, row, col, grid, mem):
  if i == row - 1:
    return 1
  if (i, j) in mem:
    return mem[(i, j)]
  val = 0
  if grid[i][j] == '.':
    val = backtrack(i + 1, j, row, col, grid, mem)
  else:
    val = backtrack(i + 1, j - 1, row, col, grid, mem) + backtrack(i + 1, j + 1, row, col, grid, mem)
  mem[(i, j)] = val
  return val

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
