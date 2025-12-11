import sys
import os
import math

# https://adventofcode.com/2025/day/10

def partOne():
  machines = parseInput()
  sum = 0
  for machine in machines:
    target, buttons, _ = machine
    sum += find_min_press(target, buttons)
  print(sum)

def find_min_press(target, buttons):
  length = len(buttons)
  # [.##.] -> (1, 2) once ideally
  # observations
  # [1,2], [2, 3] -> [1,3] using two presses
  # pressing a button more than once never helps, either no press or one press
  # this means we can brute force in O(2^n) where n is # of buttons
  # start with smaller sets to return early once a combination is found
  combos = [[set(), set()]]
  target_set = set()
  for idx in range(len(target)):
    if target[idx] == 1:
      target_set.add(idx)
  for k in range(length):
    next_combos = []
    for combo in combos:
      combo_buttons, combo_lights = combo
      for b in range(length):
        if b not in combo_buttons:
          next_combo_buttons = combo_buttons.union({b})
          next_combo_lights = combo_lights.symmetric_difference(buttons[b]) 
          next_combos.append([next_combo_buttons, next_combo_lights])
          if target_set == next_combo_lights:
            return k + 1
    combos = next_combos
  raise Exception("Woooot!")

def partTwo():
  machines = parseInput()
  sum = 0
  for machine in machines:
    _, buttons, target = machine
    curr_min = find_min_press2(0, target, buttons)
    print(curr_min)
    sum += curr_min
  print(sum)

def find_min_press2(b, target, buttons):
  # (3) (1,3) (2) (2,3) (0,2) (0,1)
  # {0:3, 1:5, 2:4, 3:7}
  # traverse buttons from left to right
  # for each button consider 0 to max possible presses given the current target
  # for 0 to max update the current target for the next button
  # return min # of presses
  if b == len(buttons):
    return 0 if all_zero(target) else sys.maxsize

  button = buttons[b]
  min_press = sys.maxsize
  # print(b, target, buttons, max_press(button, target))
  
  for press in range(max_press(button, target) + 1):
    update_target(press, button, target)
    sub_press = find_min_press2(b + 1, target, buttons)
    min_press = min(min_press, press + sub_press)
    update_target(-press, button, target)
  
  return min_press

def update_target(press, button, target):
  for idx in button:
    target[idx] -= press

def max_press(button, target):
  nums = [target[idx] for idx in button]
  min_press = nums[0]
  for num in nums:
    min_press = min(min_press, num)
  return min_press

def all_zero(target):
  for t in target:
    if t != 0:
      return False
  return True

def parseInput():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  lines = open(f'{dir_path}/input.txt', 'r').read().splitlines()
  machines = []
  for line in lines:
    parts = line.split()
    target, buttons, joltage = parts[0], parts[1:-1], parts[-1]
    m_target = [0 if light == '.' else 1 for light in target[1:-1]]
    m_buttons = [set([int(wire) for wire in button[1:-1].split(',')]) for button in buttons]
    m_joltage = [int(jolt) for jolt in joltage[1:-1].split(',')]
    machines.append([m_target, m_buttons, m_joltage])
  return machines

if sys.argv[1] == 'one':
  partOne()

if sys.argv[1] == 'two':
  partTwo()
