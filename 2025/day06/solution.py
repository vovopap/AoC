import sys
import os

# https://adventofcode.com/2025/day/6

def partOne():
  lines, last_line = parseInput()
  grid = [[int(num) for num in line.split()] for line in lines]
  ops = last_line.split()
  row = len(grid)
  col = len(grid[0])
  res = 0
  for j in range(col):
    curr = 0 if ops[j] == '+' else 1
    for i in range(row):
      if ops[j] == '+':
        curr += grid[i][j]
      else:
        curr *= grid[i][j]
    res += curr
  print(res)

def partTwo():
  lines, ops = parseInput()
  row = len(lines)
  col = len(lines[0])
  nums = [0] * col
  for line in lines:
    for i in range(col):
      ch = line[i]
      if ch == ' ':
        continue
      nums[i] = nums[i] * 10 + int(ch)
  sum = 0
  op = ops[0]
  curr = nums[0]
  for i in range(1, col):
    if ops[i] != ' ':
      sum += curr
      curr = nums[i]
      op = ops[i]
      continue
    if nums[i] != 0:
      curr = (curr * nums[i]) if op == '*' else (curr + nums[i])
  sum += curr
  print(sum)

  

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  lines = open(f'{dir_path}/input.txt', 'r').read().splitlines()
  return lines[:-1], lines[-1]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
