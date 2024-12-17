import sys
import os

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)
# https://adventofcode.com/2024/day/15

dirs = {
  '^': [-1, 0],
  '>': [0, 1],
  'v': [1, 0],
  '<': [0, -1]
}
global_min = -1
def partOne():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  # for line in grid:
  #   print(line)
  
  i, j = find_letter(grid, 'S', row, col)
  ti, tj = find_letter(grid, 'E', row, col)
  
  grid[i][j] = '#'
  backtrack(grid, i, j, ti, tj, '>', row, col, 0)
  print(global_min)

def backtrack(grid, i, j, ti, tj, move, row, col, score):
  global global_min
  if i == ti and j == tj:
    if global_min == -1:
      global_min = score
    else:
      global_min = min(global_min, score)
    return
  
  # no point going forward if already doing worse than global min
  if global_min > -1 and score > global_min:
    return
  
  for key in dirs:
    dir = dirs[key]
    ii = i + dir[0]
    jj = j + dir[1]
    if ii < 0 or ii >= row or jj < 0 or jj >= col or grid[ii][jj] == '#':
      continue
    
    # print(key)
    old = grid[ii][jj]
    grid[ii][jj] = '#'
    backtrack(grid, ii, jj, ti, tj, key, row, col, score + (1 if move == key else 1001))
    grid[ii][jj] = old  
    
def find_letter(grid, letter, row, col):
  for i in range(row):
    for j in range(col):
      if grid[i][j] == letter:
        return i, j
  return -1, -1

def partTwo():
  grid = parseInput()

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()