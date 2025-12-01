import sys
import os

# https://adventofcode.com/2025/day/1

def partOne():
  count = 0
  rotations = parseInput()
  curr = 50
  for rotation in rotations:
    curr += rotation
    # normalize
    curr %= 100
    if curr == 0:
      count += 1
  print(count)
  
  
def partTwo():
  count = 0
  rotations = parseInput()
  curr = 50
  for rotation in rotations:
    full = abs(rotation) // 100
    count += full
    leftover = abs(rotation) % 100
    if curr != 0:
      if rotation > 0:
        if leftover >= 100 - curr:
          count += 1
      else:
        if leftover >= curr:
          count += 1

    if rotation > 0:
      curr += leftover
    else:
      curr -= leftover
    # normalize
    curr %= 100
  print(count)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))  
  input = open(f'{dir_path}/input.txt', 'r').read()
  dirs = {'L': -1, 'R': 1}
  return [dirs[row[0]] * int(row[1:]) for row in input.splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()