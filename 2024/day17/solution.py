import sys
import os

# https://adventofcode.com/2024/day/17

def partOne():
  A, B, C, ops = parseInput()
  out = calc(A, B, C, ops)
  for val in out:
    print(val, end=",")

def calc(A, B, C, ops):
  pp = 0
  out = []
  while True:
    if pp >= len(ops):
      break
    op = ops[pp]
    val = ops[pp + 1]
    if op == 0:
      # adv
      A = A // (2 ** combo(val, A, B, C))
    elif op == 1:
      # bxl
      B = val ^ B
    elif op == 2:
      # bst
      B = combo(val, A, B, C) % 8
    elif op == 3:
      # jnz
      pp = val - 2 if A else pp
    elif op == 4:
      # bxc
      B = B ^ C
    elif op == 5:
      # out
      out.append(combo(val, A, B, C) % 8)
    elif op == 6:
      # bdv
      B = A // (2 ** combo(val, A, B, C))
    else:
      # cdv
      C = A // (2 ** combo(val, A, B, C))
    pp += 2
  
  return out

def combo(val, A, B, C):
  return [val, val, val, val, A, B, C][val]

def partTwo():
  A, B, C, ops = parseInput()
  curr = [(1, 0)]
  for i, a in curr:
    for a in range(a, a + 8):
      if calc(a, 0, 0, ops) == ops[-i:]:
        curr.append((i + 1, a * 8))
        if i == len(ops): print(a)

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  registers, program = open(f'{dir_path}/input.txt', 'r').read().split("\n\n")
  A, B, C = [int(line[12:]) for line in registers.splitlines()]
  ops = [int(num) for num in program.strip()[9:].split(",")]
  return A, B, C, ops

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()