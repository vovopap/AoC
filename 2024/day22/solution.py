import sys
import os

# https://adventofcode.com/2024/day/22

def partOne():
  secrets = parseInput()
  for k in range(2000):
    for i in range(len(secrets)):
      secret = secrets[i]
      step1 = secret * 64
      step1 = step1 ^ secret
      step1 = step1 % 16777216
      step2 = step1 // 32
      step2 = step2 ^ step1
      step2 = step2 % 16777216
      step3 = step2 * 2048
      step3 = step3 ^ step2
      step3 = step3 % 16777216
      secrets[i] = step3
  # print(secrets)
  res = 0
  for secret in secrets:
    res += secret
  print(res)

def partTwo():
  secrets = parseInput()
  # print(secrets)
  # put the fist value for each sequence in map and keep the count
  # 9999 * 2
  sum = {}
  for i in range(len(secrets)):
    last = []
    for k in range(2000):
      if len(last) == 5:
        last.pop(0)
      secret = secrets[i]
      step1 = secret * 64
      step1 = step1 ^ secret
      step1 = step1 % 16777216
      step2 = step1 // 32
      step2 = step2 ^ step1
      step2 = step2 % 16777216
      step3 = step2 * 2048
      step3 = step3 ^ step2
      step3 = step3 % 16777216
      secrets[i] = step3
      last.append(step3 % 10)
      if len(last) < 5:
        continue
      tup = diff(last)
      if tup not in sum:
        sum[tup] = {}
      if i not in sum[tup]:
        sum[tup][i] = last[4]
  
  res = 0
  for tup in sum:
    prices = sum[tup]
    total = 0
    for key in prices:
      total += prices[key]
    res = max(res, total)
  
  print(res)

def diff(nums):
  return (nums[1] - nums[0], nums[2] - nums[1], nums[3] - nums[2], nums[4] - nums[3])

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [int(line) for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()