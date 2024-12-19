import sys
import os

# https://adventofcode.com/2024/day/19

def partOne():
  patterns, designs = parseInput()
  # backtrack
  res = 0
  for design in designs:
    if backtrack(design, 0, patterns):
      res += 1
  print(res)

def backtrack(design, i, patterns):
  dlen = len(design)
  if dlen == i:
    return True
  
  for pattern in patterns:
    plen = len(pattern)
    if dlen - i < plen:
      continue
    if design[i:i+plen] == pattern:
      if backtrack(design, i + plen, patterns):
        return True
  
  return False

def partTwo():
  patterns, designs = parseInput()
  # backtrack with word tree
  tree = word_tree(patterns)
  memo = {}
  res = 0
  for design in designs:
    print(design)
    res += backtrack2(design, 0, tree, memo)
  print(res)
  
def backtrack2(design, i, tree, memo):
  dlen = len(design)
  if dlen == i:
    return 1
  
  rem = design[i:]
  if rem in memo:
    return memo[rem]
  
  count = 0
  next = tree
  k = i
  while k < dlen and design[k] in next['ch']:
    letter = design[k]
    next = next['ch'][letter]
    if next['valid']:
      count += backtrack2(design, k + 1, tree, memo)
    k += 1
  
  memo[design[i:]] = count
  
  return count

def word_tree(patterns):
  tree = {
    'valid': False,
    'ch': {}
  }
  for pattern in patterns:
    add_word(pattern, tree)

  return tree

def add_word(pattern, tree):
  next = tree
  for i in range(len(pattern)):
    letter = pattern[i]
    if not letter in next['ch']:
      next['ch'][letter] = {'valid': False, 'ch': {}}
    next = next['ch'][letter]
  next['valid'] = True 

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  section1, section2 = open(f'{dir_path}/input.txt', 'r').read().split("\n\n")
  patterns = section1.split(", ")
  designs = section2.splitlines()
  return patterns, designs

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()