import sys
import os
from functools import cmp_to_key

# https://adventofcode.com/2025/day/5

def partOne():
  ranges, ings = parseInput()
  count = 0
  for ing in ings:
    if is_fresh(ing, ranges):
      count += 1
  print(count)

def is_fresh(num, ranges):
  for r in ranges:
    if r[0] <= num and num <= r[1]:
      return True
  return False

def partTwo():
  ranges, ings = parseInput()
  ranges = sorted(ranges, key=cmp_to_key(compare))
  sum = 0
  curr = 0
  for r in ranges:
    left, right = r
    if right < curr:
      continue
    if left > curr:
      curr = left
    sum += right - curr + 1
    curr = right + 1
  print(sum)

def compare(a, b):
  if a[0] == b[0]:
    return a[1] - b[1]
  return a[0] - b[0]

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  part1, part2 = open(f'{dir_path}/input.txt', 'r').read().split('\n\n')
  rows = part1.splitlines()
  ranges = []
  for row in rows:
    left, right = row.split('-')
    ranges.append((int(left), int(right)))
  ings = [int(line) for line in part2.splitlines()]
  return ranges, ings

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
