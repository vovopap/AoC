import sys
import os
from functools import cmp_to_key
import math
from collections import deque

# https://adventofcode.com/2025/day/8

def partOne():
  points = parseInput()
  length = len(points)
  pairs = []
  for i in range(length):
    for j in range(i + 1, length):
      pairs.append((i, j, dist(points[i], points[j])))
  pairs = sorted(pairs, key=cmp_to_key(compare))  
  parents = {i: i for i in range(length)}
  for i in range(1000):
    u, v, _ = pairs[i]
    pu = get_parent(u, parents)
    pv = get_parent(v, parents)
    if pu != pv: # different parents
      parents[pv] = pu

  count = {}
  for node in range(length):
    p = get_parent(node, parents)
    if p not in count:
      count[p] = 1
    else:
      count[p] += 1
  res = 1
  for g in sorted(list(set(count.values())))[-3:]:
    res *= g
  print(res)

def get_parent(node, parents):
  while node != parents[node]:
    node = parents[node]
  return node

def dist(p, q):
  sum = 0
  for i in range(3):
    sum += (p[i] - q[i]) ** 2
  return math.sqrt(sum)

def compare(a, b):
  return a[2] - b[2]

def partTwo():
  points = parseInput()
  length = len(points)
  pairs = []
  for i in range(length):
    for j in range(i + 1, length):
      pairs.append((i, j, dist(points[i], points[j])))
  pairs = sorted(pairs, key=cmp_to_key(compare))

  parents = {i: i for i in range(length)}
  children = {i: 1 for i in range(length)}
  for pair in pairs:
    u, v, _ = pair
    pu = get_parent(u, parents)
    pv = get_parent(v, parents)
    if pu != pv: # different parents
      parents[pv] = pu
      children[pu] += children[pv]
      if children[pu] == length:
        print(points[u][0] * points[v][0])

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [[int(num) for num in line.split(',')] for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
