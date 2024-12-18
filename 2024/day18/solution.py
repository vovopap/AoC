import sys
import os

# https://adventofcode.com/2024/day/18

def partOne():
  falls = parseInput()
  row = 71
  col = 71
  blocks = set()
  for idx in range(1024):
    j, i = falls[idx]
    blocks.add(i * col + j)
  
  dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  # bfs
  seen = set()
  q = [(0, 0)]
  levels = 0
  while len(q) != 0:
    levels += 1
    q_size = len(q)
    for idx in range(q_size):
      i, j = q.pop(0)
      for dir in dirs:
        ii = i + dir[0]
        jj = j + dir[1]
        if ii < 0 or ii >= row or jj < 0 or jj >= col or (ii * col + jj) in seen:
          continue
        if (ii * col + jj) not in blocks:
          if ii == 70 and jj == 70:
            print(levels)
            return
          seen.add(ii * col + jj)
          q.append([ii, jj])
    

def partTwo():
  falls = parseInput()
  row = 71
  col = 71
  blocks = set()
  for idx in range(1024):
    j, i = falls[idx]
    blocks.add(i * col + j)
  
  for idx in range(1024, len(falls)):
    j, i = falls[idx]
    blocks.add(i * col + j)
    if not bfs(blocks, row, col):
      print(j, i)
      break
  
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(blocks, row, col):
  seen = set()
  q = [(0, 0)]
  levels = 0
  while len(q) != 0:
    levels += 1
    q_size = len(q)
    for idx in range(q_size):
      i, j = q.pop(0)
      for dir in dirs:
        ii = i + dir[0]
        jj = j + dir[1]
        if ii < 0 or ii >= row or jj < 0 or jj >= col or (ii * col + jj) in seen:
          continue
        if (ii * col + jj) not in blocks:
          if ii == 70 and jj == 70:
            return True
          seen.add(ii * col + jj)
          q.append([ii, jj])
  return False

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [[int(coor) for coor in line.split(",")] for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()