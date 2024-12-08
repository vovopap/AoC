import sys
import os
from functools import cmp_to_key

# https://adventofcode.com/2024/day/7

def partOne():
  eqs = parseInput()
  # print(eqs)
  count = 0
  for eq in eqs:
    answer = eq[0]
    nums = eq[1]
    if recur(answer, nums, len(nums) - 1):
      count += answer
  print(count)

def recur(answer, nums, n):
  if (n < 0):
    return False
  
  num = nums[n]
  if answer < 0:
    return False
  
  if n == 0 and answer == num:
    return True
  
  valid = False
  if answer % num == 0:
    valid = recur(answer // num, nums, n - 1)
  if not valid:
    valid = recur(answer - num, nums, n - 1)
  if not valid and n >= 1:
    valid = recur(int(str(answer) + "" + str(num)), nums, n - 2)
  
  return valid
  
def partTwo():
  eqs = parseInput()
  # print(eqs)
  count = 0
  for eq in eqs:
    answer = eq[0]
    nums = eq[1]
    if recur2(nums[0], answer, nums, 1):
      count += answer
  print(count)
  
def recur2(curr, answer, nums, n):
  if (n == len(nums)) and curr == answer:
    return True
  
  if (n == len(nums)):
    return False
  
  num = nums[n]  
  valid = recur2(curr + num, answer, nums, n + 1)
  if not valid:
    valid = recur2(curr * num, answer, nums, n + 1)
  if not valid:
    valid = recur2(int(str(curr) + str(num)), answer, nums, n + 1)
  
  return valid

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  eqs = [line.split(": ") for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]
  for i in range(len(eqs)):
    eqs[i][0] = int(eqs[i][0])
    eqs[i][1] = [int(num) for num in eqs[i][1].split(" ")]
  return eqs

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()