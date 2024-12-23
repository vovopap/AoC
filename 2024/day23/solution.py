import sys
import os

# https://adventofcode.com/2024/day/23

def partOne():
  connections = parseInput()
  conn = {}
  uniq = set()
  for connection in connections:
    a, b = connection
    if a not in conn:
      conn[a] = set()
    if b not in conn:
      conn[b] = set()
    conn[a].add(b)
    conn[b].add(a)
    uniq.add(a)
    uniq.add(b)
  uniq = list(uniq)
  size = len(uniq)
  three = []
  for i in range(size):
    for j in range(i + 1, size):
      for k in range(j + 1, size):
        a, b, c = uniq[i], uniq[j], uniq[k]
        if a in conn[b] and a in conn[c] and b in conn[c]:
          three.append((a, b, c))
  res = 0
  for tup in three:
    a, b, c = tup
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
      res += 1
  print(res)
def partTwo():
  connections = parseInput()
  graph = {}
  for connection in connections:
    a, b = connection
    if a not in graph:
      graph[a] = set()
    if b not in graph:
      graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

  all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
  maxx = set()
  for cl in all_cliques:
    if len(cl) > len(maxx):
      maxx = cl
  for item in sorted(list(maxx)):
    print(item, end=",")

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)

def diff(nums):
  return (nums[1] - nums[0], nums[2] - nums[1], nums[3] - nums[2], nums[4] - nums[3])

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [line.split("-") for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()