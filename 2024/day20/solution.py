import sys
import os

# https://adventofcode.com/2024/day/20

def partOne():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  # bfs
  si, sj = find_letter('S', grid, row, col)
  ei, ej = find_letter('E', grid, row, col)
  dist = bfs(grid, si, sj, row, col)
  grid[si][sj] = '.'
  grid[ei][ej] = '.'
  
  res = 0
  for i in range(row):
    # 1x
    for j in range(1, col - 1):
      if grid[i][j] == '#' and grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
        if abs(dist[i][j - 1] - dist[i][j + 1]) - 2 >= 100:
          res += 1
    # 2x
    for j in range(1, col - 2):
      if grid[i][j] == '#' and grid[i][j + 1] == '#' and grid[i][j - 1] == '.' and grid[i][j + 2] == '.':
        if abs(dist[i][j - 1] - dist[i][j + 2]) - 3 >= 100:
          res += 1
  for j in range(col):
    # 1x
    for i in range(1, row - 1):
      if grid[i][j] == '#' and grid[i - 1][j] == '.' and grid[i + 1][j] == '.':
        if abs(dist[i - 1][j] - dist[i + 1][j]) - 2 >= 100:
          res += 1
    # 2x
    for i in range(1, row - 2):
      if grid[i][j] == '#' and grid[i + 1][j] == '#' and grid[i - 1][j] == '.' and grid[i + 2][j] == '.':
        if abs(dist[i - 1][j] - dist[i + 2][j]) - 3 >= 100:
          res += 1
  print(res)

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(grid, si, sj, row, col):
  dist = [[-1 for j in range(col)] for i in range(row)]
  q = [(si, sj)]
  seen = set()
  seen.add((si, sj))
  levels = 0
  while len(q) != 0:
    q_size = len(q)
    for idx in range(q_size):
      i, j = q.pop(0)
      dist[i][j] = levels
      for dir in dirs:
        ii = i + dir[0]
        jj = j + dir[1]
        if ii < 0 or ii >= row or jj < 0 or jj >= col or grid[ii][jj] == '#' or (ii, jj) in seen:
          continue
        seen.add((ii, jj))
        q.append((ii, jj))
    levels += 1
  return dist

def find_letter(letter, grid, row, col):
  for i in range(row):
    for j in range(col):
      if grid[i][j] == letter:
        return i, j
  return -1, -1

def partTwo():
  grid = parseInput()
  row = len(grid)
  col = len(grid[0])
  # bfs
  si, sj = find_letter('S', grid, row, col)
  ei, ej = find_letter('E', grid, row, col)
  dist = bfs(grid, si, sj, row, col)
  grid[si][sj] = '.'
  grid[ei][ej] = '.'
  
  res = 0
  # from each point run bfs up to 1, 2, 3, .., 20 steps
  # add the coors which give at least 100 saves
  for i in range(row):
    for j in range(col):
      if grid[i][j] == '.':
        res += bfs2(grid, i, j, dist, row, col, 100)
  print(res / 2)

def bfs2(grid, si, sj, dist, row, col, min_save):
  print("bfs2", si, sj)
  res = 0
  q = [(si, sj)]
  seen = set()
  seen.add((si, sj))
  levels = 0
  while len(q) != 0:
    q_size = len(q)
    for idx in range(q_size):
      i, j = q.pop(0)
      if grid[i][j] == '.' and (abs(dist[si][sj] - dist[i][j]) - levels) >= min_save:
        res += 1
      for dir in dirs:
        ii = i + dir[0]
        jj = j + dir[1]
        if ii < 0 or ii >= row or jj < 0 or jj >= col or (ii, jj) in seen:
          continue
        seen.add((ii, jj))
        q.append((ii, jj))
    levels += 1
    if levels > 20:
      break
  return res # 1150073 is too high
def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()