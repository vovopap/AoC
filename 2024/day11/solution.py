import sys
import os

# https://adventofcode.com/2024/day/10

def partOne():
  nums = parseInput()
  for i in range(25):
    next = []
    for num in nums:
      if num == 0:
        next.append(1)
      elif len(str(num)) % 2 == 0:
        num_str = str(num)
        size = len(num_str)
        next.append(int(num_str[:size // 2]))
        next.append(int(num_str[size // 2:]))
      else:
        next.append(num * 2024)
    nums = next
  print(len(nums))

def partTwo():
  nums = parseInput()
  count = 0
  meme = {}
  for num in nums:
    count += recur(num, meme, 25)
  print(count)

def recur(num, meme, blink):
  if blink == 0:
    return 1
  
  if num in meme and blink in meme[num]:
    return meme[num][blink]
  
  next = []
  if num == 0:
    next.append(1)
  elif len(str(num)) % 2 == 0:
    num_str = str(num)
    size = len(num_str)
    next.append(int(num_str[:size // 2]))
    next.append(int(num_str[size // 2:]))
  else:
    next.append(num * 2024)
  
  count = 0
  for n in next:
    count += recur(n, meme, blink - 1)
  
  if num not in meme:
    meme[num] = {}
  
  meme[num][blink] = count
  
  return count


def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [int(num) for num in open(f'{dir_path}/input.txt', 'r').read().strip().split(" ")]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()