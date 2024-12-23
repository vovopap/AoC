import sys
import os

# https://adventofcode.com/2024/day/21

def partOne():
  codes = parseInput()
  # numeric keypad <- directional keypad <- directional keypad <- my keypad
  print(codes)
  res = 0
  for code in codes:
    count = 0
    for key in code:
      count += numeric(key)
    res += count * int(code[:-1])

def numeric(key):
  

def partTwo():
  grid = parseInput()
  
def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return open(f'{dir_path}/input.txt', 'r').read().splitlines()

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()