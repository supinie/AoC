from math import inf
from collections import Counter
from get_input import *

url = "https://adventofcode.com/2021/day/3/input"
gammaList = [[], [], [], [], [], [], [], [], [], [], [], []]
gamma = []
epsilon = []

text = get_input(url)

for i in text:
    instructions = i

instructions = instructions.split("\n")
instructions.pop()

for i in range(0, len(instructions) - 1):
    for j in range(0, 12):
        gammaList[j].append(instructions[i][j])

for i in range(0, len(gammaList)):
    gamma.append(max(set(gammaList[i]), key=gammaList[i].count))
    epsilon.append(min(set(gammaList[i]), key=gammaList[i].count))

gamma = "".join(gamma)
epsilon = "".join(epsilon)

result = int(gamma, 2)*int(epsilon, 2)

print(result)

