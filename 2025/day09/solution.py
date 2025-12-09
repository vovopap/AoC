import sys
import os
import math

# https://adventofcode.com/2025/day/9

def partOne():
  points = parseInput()
  length = len(points)
  max_area = 0
  for i in range(length):
    for j in range(i + 1, length):
      area = calc_area(points[i], points[j])
      max_area = area if area > max_area else max_area
  print(max_area)

def calc_area(a, b):
  x = 0
  y = 1
  return (abs(a[x] - b[x]) + 1) * (abs(a[y] - b[y]) + 1)

def partTwo():
  points = parseInput()
  length = len(points)
  # for points a and b
  # ensure all the other points are inside the rectange formed by a and b
  # take max of all such pairs of points
  max_area = 0
  for i in range(length):
    for j in range(i + 1, length):
      if valid(i, j, points):
        area = calc_area(points[i], points[j])
        max_area = area if area > max_area else max_area
        
  print(max_area)

# the algo does not work well if the polygon has inside curves
# the reason the below algo was good enough because the AoC input does not have rectanges formed by inside curves...
# whose area is bigger than the area of valid rectangles
def valid(i, j, points):
  length = len(points)
  pi = points[i]
  pj = points[j]
  x = 0
  y = 1
  # ensure all the other points are inside the rectange formed by a and b
  x_min = min(pi[x], pj[x])
  x_max = max(pi[x], pj[x])
  y_min = min(pi[y], pj[y])
  y_max = max(pi[y], pj[y])
  for k in range(length):
    a, b = points[k], points[(k + 1) % length]
    
    if a[x] == b[x] and between_strict(a[x], x_min, x_max): # vertical
      low_y = min(a[y], b[y])
      high_y = max(a[y], b[y])
      if not (high_y <= y_min or y_max <= low_y):
        return False
    
    if a[y] == b[y] and between_strict(a[y], y_min, y_max): # horizontal
      low_x = min(a[x], b[x])
      high_x = max(a[x], b[x])
      if not (high_x <= x_min or x_max <= low_x):
        return False

  return True

def between(val, min, max):
  return min <= val and val <= max

def between_strict(val, min, max):
  return min < val and val < max

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [[int(num) for num in line.split(',')] for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
