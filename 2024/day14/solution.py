import sys
import os
from functools import cmp_to_key

# https://adventofcode.com/2024/day/14

x = 0
y = 1
mx, mx2 = 101, 50
my, my2 = 103, 51
def partOne():
  robots = parseInput()
  print(robots)
  q1, q2, q3, q4 = 0, 0, 0, 0
  for robot in robots:
    p0, v = robot
    p = [p0[x] + v[x] * 100, p0[y] + v[y] * 100]
    if p[x] >= 0:
      p[x] = p[x] % mx
    else:
      p[x] = (mx - abs(p[x])) % mx
      
    if p[y] >= 0:
      p[y] = p[y] % my
    else:
      p[y] = (my - abs(p[y])) % my
    
    if p[x] < mx2:
      if p[y] < my2:
        q1 += 1
      elif p[y] > my2:
        q2 += 1
    elif p[x] > mx2:
      if p[y] < my2:
        q3 += 1
      elif p[y] > my2:
        q4 += 1
    print(p0, v, p)
  print(q1 * q2 * q3 * q4)

def partTwo():
  robots = parseInput()
  levels = []
  for s in range(10000):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(len(robots)):
      robot = robots[i]
      p0, v = robot
      p = wrap([p0[x] + v[x], p0[y] + v[y]])
      robots[i][0] = p
      if p[x] < mx2:
        if p[y] < my2:
          q1 += 1
        elif p[y] > my2:
          q2 += 1
      elif p[x] > mx2:
        if p[y] < my2:
          q3 += 1
        elif p[y] > my2:
          q4 += 1
    levels.append([q1 * q2 * q3 * q4, s])
  levels = sorted(levels, key=cmp_to_key(compare))
  
  for i in range(10):
    print(levels[i])

def compare(a, b):
  return a[0] - b[0]

def wrap(p):
  if p[x] >= 0:
    p[x] = p[x] % mx
  else:
    p[x] = (mx - abs(p[x])) % mx

  if p[y] >= 0:
    p[y] = p[y] % my
  else:
    p[y] = (my - abs(p[y])) % my
  return p

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  items = open(f'{dir_path}/input.txt', 'r').read().splitlines()
  robots = []
  for item in items:
    P, V = item.split(" ")
    p = [int(num) for num in P[2:].split(",")]
    v = [int(num) for num in V[2:].split(",")]
    robots.append([p, v])
  return robots

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()