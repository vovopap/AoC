import sys
import os

# https://adventofcode.com/2024/day/12

def partOne():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  print(grid)
  res = 0
  visited = [[False for j in range(col)] for i in range(row)]
  for i in range(row):
    for j in range(col):
      if visited[i][j]:
        continue
      perimeter, area = spread1(grid, grid[i][j], i, j, visited, row, col)
      multi = perimeter * area
      res += multi
  print(res)
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
diagonal = [[-1, 1], [1, 1], [1, -1], [-1, -1]]

def spread1(grid, letter, i, j, visited, row, col):
  visited[i][j] = True
  # check 4 corners
  perimeter = 0
  area = 1
  for dir in dirs:
    ii = i + dir[0]
    jj = j + dir[1]
    if ii < 0 or ii >= row or jj < 0 or jj >= col or grid[ii][jj] != letter:
      perimeter += 1
      continue
    
    if not visited[ii][jj]:
      p, a = spread1(grid, letter, ii, jj, visited, row, col)
      perimeter += p
      area += a
  return perimeter, area

def partTwo():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  print(grid)
  res = 0
  visited = [[False for j in range(col)] for i in range(row)]
  for i in range(row):
    for j in range(col):
      if visited[i][j]:
        continue
      corner, area = spread2(grid, grid[i][j], i, j, visited, row, col)
      multi = corner * area
      res += multi
  print(res)

def spread2(grid, letter, i, j, visited, row, col):
  visited[i][j] = True
  corner = 0
  area = 1
  # check 4 outer and inner corners
  for k in range(4):
    n = (k + 1) % 4
    Ai = i + dirs[k][0]
    Aj = j + dirs[k][1]
    Bi = i + dirs[n][0]
    Bj = j + dirs[n][1]
    if (off_grid(Ai, Aj, row, col) or grid[Ai][Aj] != letter) and (off_grid(Bi, Bj, row, col) or grid[Bi][Bj] != letter):
      corner += 1
    
    Ci = i + diagonal[k][0]
    Cj = j + diagonal[k][1]
    if not off_grid(Ai, Aj, row, col) and grid[Ai][Aj] == letter and \
      not off_grid(Bi, Bj, row, col) and grid[Bi][Bj] == letter and \
      not off_grid(Ci, Cj, row, col) and grid[Ci][Cj] != letter:
        corner += 1
    
  for dir in dirs:
    ii = i + dir[0]
    jj = j + dir[1]
    if off_grid(ii, jj, row, col) or grid[ii][jj] != letter:
      continue
    
    if not visited[ii][jj]:
      c, a = spread2(grid, letter, ii, jj, visited, row, col)
      corner += c
      area += a
  return corner, area

def off_grid(i, j, row, col):
  return i < 0 or i >= row or j < 0 or j >= col

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()