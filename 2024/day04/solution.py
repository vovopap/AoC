import sys
import os

# https://adventofcode.com/2024/day/4

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
word = 'XMAS'
def partOne():
  grid = parseInput()
  # do DFS from all Xs
  # count them
  row = len(grid)
  col = len(grid[0])
  count = 0
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 'X':
        for dir in dirs:
          count += dfs(grid, i, j, 1, dir, row, col)
  
  print(count)

def partTwo():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  # [1, 1], [-1, -1], [1, -1], [-1, 1]
  lt = [-1, -1]
  rb = [1, 1]
  rt = [-1, 1]
  lb = [1, -1]
  count = 0
  for i in range(1, row - 1):
    for j in range(1, col - 1):
      if grid[i][j] == 'A':
        one = grid[i + lt[0]][j + lt[1]] + 'A' + grid[i + rb[0]][j + rb[1]]
        two = grid[i + rt[0]][j + rt[1]] + 'A' + grid[i + lb[0]][j + lb[1]]
        if (one == 'MAS' or one == 'SAM') and (two == 'MAS' or two == 'SAM'):
          count += 1
  print(count)
        
        


def dfs(grid, i, j, n, dir, row, col):
  if n == 4:
    return 1
  curr = word[n]
  ii = i + dir[0]
  jj = j + dir[1]
  if ii >= 0 and ii < row and jj >= 0 and jj < col and grid[ii][jj] == curr:
    return dfs(grid, ii, jj, n + 1, dir, row, col)
  return 0

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))  
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()