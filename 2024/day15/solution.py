import sys
import os

# https://adventofcode.com/2024/day/15

dirs = {
  '^': [-1, 0],
  '>': [0, 1],
  'v': [1, 0],
  '<': [0, -1]
}

def partOne():
  grid, moves = parseInput()
  row = len(grid)
  col = len(grid[0])
  si, sj = robot_position(grid, row, col)
  for move in moves:
    dir = dirs[move]
    ni, nj = si, sj
    while True:
      ni, nj = ni + dir[0], nj + dir[1]
      if grid[ni][nj] == '.':
        break
      elif grid[ni][nj] == '#':
        break
    if grid[ni][nj] == '.':
      while not (ni == si and nj == sj):
        grid[ni][nj] = grid[ni - dir[0]][nj - dir[1]]
        ni, nj = ni - dir[0], nj - dir[1]
      grid[si][sj] = '.'
      si, sj = si + dir[0], sj + dir[1]
  res = 0
  for i in range(row):
    for j in range(col):
      if grid[i][j] == 'O':
        res += i * 100 + j
  print(res)

def robot_position(grid, row, col):
  for i in range(row):
    for j in range(col):
      if grid[i][j] == '@':
        return i, j
  
  return -1, -1

def partTwo():
  grid, moves = parseInput()
  grid = widen(grid)
  row = len(grid)
  col = len(grid[0])
  si, sj = robot_position(grid, row, col)
  for i in range(len(moves)):
    move = moves[i]
    if can_move(grid, si, sj, move):
      si, sj = move_it(grid, si, sj, move)
  res = 0
  for i in range(row):
    for j in range(col):
      if grid[i][j] == '[':
        res += i * 100 + j
  print(res)

def can_move(grid, si, sj, move):
  dir = dirs[move]
  ni, nj = si + dir[0], sj + dir[1]
  n = grid[ni][nj]
  if n == '#':
    return False
  
  if n == '.':
    return True
  
  # left and right is simple
  if move == '<' or move == '>':
    return can_move(grid, ni, nj, move)
  
  # top and bottom is tricky
  if n == '[':
    # check if '[' can be moved
    # check if ']' can be moved
    return can_move(grid, ni, nj, move) and can_move(grid, ni, nj + 1, move)
  return can_move(grid, ni, nj, move) and can_move(grid, ni, nj - 1, move)

def move_it(grid, si, sj, move):
  dir = dirs[move]
  ni, nj = si + dir[0], sj + dir[1]
  s = grid[si][sj]
  n = grid[ni][nj]
  
  if n == '.':
    grid[ni][nj] = s
    grid[si][sj] = '.'
    return ni, nj
  
  # left and right is simple
  if move == '<' or move == '>':
    move_it(grid, ni, nj, move)
    grid[ni][nj] = s
    grid[si][sj] = '.'
    return ni, nj
  
  # top and bottom is tricky
  if n == '[':
    # check if '[' can be moved
    # check if ']' can be moved
    move_it(grid, ni, nj, move)
    move_it(grid, ni, nj + 1, move)
    grid[ni][nj] = s
    grid[si][sj] = '.'
    return ni, nj
  
  move_it(grid, ni, nj, move)
  move_it(grid, ni, nj - 1, move)
  grid[ni][nj] = s
  grid[si][sj] = '.'
  return ni, nj

def widen(grid):
  new_grid = []
  for i in range(len(grid)):
    line = []
    for j in range(len(grid[0])):
      val = grid[i][j]
      if val == '@':
        line.append('@')
        line.append('.')
      elif val == 'O':
        line.append('[')
        line.append(']')
      else:
        line.append(val)
        line.append(val)
    new_grid.append(line)
  return new_grid

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  grid, moves = open(f'{dir_path}/input.txt', 'r').read().split("\n\n")
  grid = [list(line) for line in grid.splitlines()]
  moves = list(moves.replace("\n", "").strip())
  return grid, moves

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()