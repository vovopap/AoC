import sys
import os

# https://adventofcode.com/2024/day/10

def partOne():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  reach = [[0 for j in range(col)] for i in range(row)]
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 9:
        seen = [[False for j in range(col)] for i in range(row)]
        spread1(grid, reach, seen, i, j, row, col)
  
  count = 0
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 0:
        count += reach[i][j]
  
  print(count)

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def spread1(grid, reach, seen, i, j, row, col):
  reach[i][j] += 1
  seen[i][j] = True
  val = grid[i][j]
  for dir in dirs:
    # print(dir)
    ii = i + dir[0]
    jj = j + dir[1]
    if ii >= 0 and ii < row and jj >= 0 and jj < col and grid[ii][jj] == val - 1 and not seen[ii][jj]:
      spread1(grid, reach, seen, ii, jj, row, col)

def partTwo():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  reach = [[0 for j in range(col)] for i in range(row)]
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 9:
        spread(grid, reach, i, j, row, col)
  
  count = 0
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 0:
        count += reach[i][j]
  
  print(count)
  
def spread(grid, reach, i, j, row, col):
  reach[i][j] += 1
  val = grid[i][j]
  for dir in dirs:
    # print(dir)
    ii = i + dir[0]
    jj = j + dir[1]
    if ii >= 0 and ii < row and jj >= 0 and jj < col and grid[ii][jj] == val - 1:
      spread(grid, reach, ii, jj, row, col)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [[int(num) for num in list(line)] for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()