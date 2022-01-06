from math import inf
from collections import Counter
from get_input import *

def findMax(myList):
    maximum = []
    for i in range(0, len(myList)):
        maximum.append(max(set(myList[i]), key=myList[i].count))
    return maximum  
def findMin(myList):
    minimum = []
    for i in range(0, len(myList)):    
        minimum.append(min(set(myList[i]), key=myList[i].count))
    return minimum

url = "https://adventofcode.com/2021/day/3/input"
gammaList = [[], [], [], [], [], [], [], [], [], [], [], []]


text = get_input(url)

for i in text:
    instructions = i

instructions = instructions.split("\n")
instructions.pop()

for i in range(0, len(instructions) - 1):
    for j in range(0, 12):
        gammaList[j].append(instructions[i][j])

gamma = findMax(gammaList)
epsilon = findMin(gammaList)

gamma = "".join(gamma)
epsilon = "".join(epsilon)

result = int(gamma, 2)*int(epsilon, 2)

print(result)
