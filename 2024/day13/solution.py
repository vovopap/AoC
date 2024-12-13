import sys
import os

# https://adventofcode.com/2024/day/13

def partOne():
  claws = parseInput()
  # Button A: X+94, Y+34
  # Button B: X+22, Y+67
  # Prize: X=8400, Y=5400
  # 94A + 22B - 8400 = 0
  # 34A + 67B - 5400 = 0
  # 22*-5400 + 67*8400 / 94*67 - 34*22
  # 562 800 - 118 800 / 6 298 - 748
  # 80
  
  # Button A: X+26, Y+66
  # Button B: X+67, Y+21
  # Prize: X=12748, Y=12176
  # 26A + 67B - 12748 = 0
  # 66A + 21B - 12176 = 0
  # 815 792 - 267 708 / 26*21-66*67
  res = 0
  a = 0
  b = 1
  c = 2
  for claw in claws:
    A, B, C = claw
    L1 = [A[0], B[0], -C[0]]
    L2 = [A[1], B[1], -C[1]]
    x0 = (L1[b] * L2[c] - L2[b] * L1[c]) / (L1[a] * L2[b] - L2[a] * L1[b])
    y0 = (L1[c] * L2[a] - L2[c] * L1[a]) / (L1[a] * L2[b] - L2[a] * L1[b])
    if x0 == int(x0) and y0 == int(y0):
      res += x0 * 3 + y0
  print(res)

def partTwo():
  claws = parseInput()
  res = 0
  a = 0
  b = 1
  c = 2
  for claw in claws:
    A, B, C = claw
    L1 = [A[0], B[0], -C[0] - 10000000000000]
    L2 = [A[1], B[1], -C[1] - 10000000000000]
    x0 = (L1[b] * L2[c] - L2[b] * L1[c]) / (L1[a] * L2[b] - L2[a] * L1[b])
    y0 = (L1[c] * L2[a] - L2[c] * L1[a]) / (L1[a] * L2[b] - L2[a] * L1[b])
    if x0 == int(x0) and y0 == int(y0):
      res += x0 * 3 + y0
  print(res)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  items = [line.splitlines() for line in open(f'{dir_path}/input.txt', 'r').read().split("\n\n")]
  claws = []
  for item in items:
    A = [int(num[2:]) for num in item[0][10:].split(", ")]
    B = [int(num[2:]) for num in item[1][10:].split(", ")]
    P = [int(num[2:]) for num in item[2][7:].split(", ")]
    claws.append([A, B, P])
  return claws

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()