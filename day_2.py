from math import inf
from get_input import *

url = "https://adventofcode.com/2021/day/2/input"
position = [0, 0, 0]

text = get_input(url)

for i in text:
    temp = i

instructions = temp.split("\n")
instructions.pop()

for i in instructions:
    if i.__contains__("forward"):
        position[0] += int(i[-1])
    elif i.__contains__("down"):
        position[1] += int(i[-1])
    elif i.__contains__("up"):
        position[1] -= int(i[-1])

print("part 1: ", position, (position[0]*position[1]))

position = [0, 0, 0]

for i in instructions:
    if i.__contains__("forward"):
        position[0] += int(i[-1])
        position[1] += int(i[-1])*position[2]
    elif i.__contains__("down"):
        position[2] += int(i[-1])
    elif i.__contains__("up"):
        position[2] -= int(i[-1])

print("part 2: ", position, (position[0]*position[1]))