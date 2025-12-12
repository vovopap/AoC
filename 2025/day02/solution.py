import sys
import os
import textwrap

# https://adventofcode.com/2025/day/2

def partOne():
  ranges = parseInput()
  sum = 0
  for r in ranges:
    start, end = r
    for curr in range(start, end + 1):
      if not validPartOne(str(curr)):
        sum += curr
  print(sum)

def validPartOne(num):
  length = len(num)
  if length % 2 == 1:
    return True
  chunks = textwrap.wrap(num, length // 2)
  return chunks[0] != chunks[1] 
  
def partTwo():
  ranges = parseInput()
  sum = 0
  for r in ranges:
    start, end = r
    for curr in range(start, end + 1):
      if not validPartTwo(str(curr)):
        sum += curr
  print(sum)

def validPartTwo(num):
  length = len(num)
  for k in range(1, length // 2 + 1):
    if length % k == 0:
      chunks = set(textwrap.wrap(num, k))
      if len(chunks) == 1:
        return False
  return True

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))  
  ranges = [r.split('-') for r in open(f'{dir_path}/input.txt', 'r').read().split(',')]
  return [(int(r[0]), int(r[1])) for r in ranges]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
