import sys
import os

# https://adventofcode.com/2024/day/24

def partOne():
  ins, gates = parseInput()
  # print(ins, gates)
  zgates = []
  for gate in gates:
    if gate[0] == 'z':
      zgates.append(gate)
  zgates = sorted(zgates)
  print(zgates)
  binary = ""
  for zgate in zgates:
    binary = str(compute(zgate, gates, ins)) + binary
  print(int(binary, base=2))

def compute(gate, gates, ins):
  if gate in ins:
    return ins[gate]
  
  op1, op, op2 = gates[gate]
  
  ins[gate] = bitwise(compute(op1, gates, ins), op, compute(op2, gates, ins))
  
  return ins[gate]

def bitwise(op1, op, op2):
  if op == 'AND':
    return op1 & op2
  elif op == 'OR':
    return op1 | op2
  else:
    return op1 ^ op2

def partTwo():
  ins, gates = parseInput()

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  section1, section2 = open(f'{dir_path}/input.txt', 'r').read().split('\n\n')
  ins = {line[:3]: int(line[5:]) for line in section1.splitlines()}
  lines = [line.split(" -> ") for line in section2.splitlines()]
  gates = {}
  for line in lines:
    left, right = line
    gates[right] = left.split(' ')
  return ins, gates

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()