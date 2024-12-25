import sys
import os

# https://adventofcode.com/2024/day/9

def partOne():
  disk = parseInput()
  # 2 _3_ 3 _3_ 1 _3_ 3 _1_ 2 _1_ 4 _1_ 4 _1_ 3 _1_ 4 _0_ 2
  size = len(disk)
  i = 0
  j = size - 1 if size % 2 == 1 else size - 2
  pos = 0
  sum = 0
  while True:
    if i > j:
      break
    left_id = i // 2
    right_id = j // 2
    left = disk[i]
    right = disk[j]
    # non-empty left block
    if i % 2 == 0:
      # calculate checksum for i
      sum += left_id * (2 * pos + left - 1) * (left / 2)
      print(sum)
      # move position
      pos += left
      i += 1
    else:
    # empty left block
      # fill i + 1 with as much of j as possible
      # calculate checksum for moved blocks
      min_val = min(left, right)
      sum += right_id * (2 * pos + min_val - 1) * (min_val / 2)
      print(sum, pos, min_val, right_id)
      pos += min_val
      if left > right:
        j -= 2
        disk[i] -= right
      elif left < right:
        i += 1
        disk[j] -= left
      else:
        j -= 2
        i += 1
  print(sum)
    

def partTwo():
  disk = parseInput()
  # 2 _3_ 3 _3_ 1 _3_ 3 _1_ 2 _1_ 4 _1_ 4 _1_ 3 _1_ 4 _0_ 2
  size = len(disk)
  dcopy = [i for i in disk]
  # block index -> set of ids located in that block
  moved = [[] for i in range(size)]
  movedj = set()
  for j in range(size - 1, 0, -2):
    right = dcopy[j]
    for i in range(1, j, 2):
      left = dcopy[i]
      if left >= right:
        moved[i].append(j)
        dcopy[i] -= right
        movedj.add(j)
        # disk[j] = 0
        print('moved', j // 2, '->', i)
        break
  
  pos = 0
  sum = 0
  for i in range(size):
    val = disk[i]
    if i % 2 == 0:
      if i not in movedj:
        id = i // 2
        sum += id * (pos + pos + val - 1) * val / 2
        print(sum)
    else:
      jpos = pos
      moves = moved[i]
      for j in moves:
        jval = disk[j]
        jid = j // 2
        sum += jid * (jpos + jpos + jval - 1) * jval / 2
        print(sum)
        jpos += jval
    pos += val
  print(disk)
  print(moved)
  print(sum)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [int(num) for num in list(open(f'{dir_path}/input.txt', 'r').read())]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()