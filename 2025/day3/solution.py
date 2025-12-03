import sys
import os

# https://adventofcode.com/2025/day/3

def partOne():
  banks = parseInput()
  sum_volt = 0
  for bank in banks:
    length = len(bank)
    k1 = 0
    for idx in range(length - 1):
      if (bank[idx] > bank[k1]):
        k1 = idx
    k2 = k1 + 1
    for idx in range(k2, length):
      if (bank[idx] > bank[k2]):
        k2 = idx
    sum_volt += bank[k1] * 10 + bank[k2]
  print(sum_volt)
  
def partTwo():
  banks = parseInput()
  sum_volt = 0
  for bank in banks:
    length = len(bank)
    max_volt = 0
    k = 0
    for offset in range(11, -1, -1): # 11, 10, ..., 0
      for idx in range(k, length - offset):
        if (bank[idx] > bank[k]):
          k = idx
      max_volt = max_volt * 10 + bank[k]
      k += 1
    sum_volt += max_volt
  print(sum_volt)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))  
  rows = [list(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]
  return [[int(num) for num in row] for row in rows]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
