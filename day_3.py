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
co2List = [[], [], [], [], [], [], [], [], [], [], [], []]


text = get_input(url)

for i in text:
    instructions = i

instructions = instructions.split("\n")
instructions.pop()

for i in range(0, len(instructions) - 1):
    for j in range(0, 12):
        gammaList[j].append(instructions[i][j])
        co2List[j].append(instructions[i][j])

gamma = findMax(gammaList)
epsilon = findMin(gammaList)

gamma = "".join(gamma)
epsilon = "".join(epsilon)

result = int(gamma, 2)*int(epsilon, 2)

print(result)


unique = 0


for i in range(0, len(gammaList)):
    unique = int(gammaList[i].count(""))
    if unique == 998:
        break
    counter = Counter(gammaList[i])
    if counter["1"] == counter["0"] or counter["1"] > counter["0"]:
        comparison = "1"
    else:
        comparison = "0"
    for j in range(0, len(gammaList[i])):
        if gammaList[i][j] != comparison:
            for k in range(0, len(gammaList)):
                gammaList[k][j] = ""

unique = 0

for i in range(0, len(co2List)):
    unique = int(co2List[i].count(""))
    if unique == 998:
        break
    counter = Counter(co2List[i])
    if counter["0"] == counter["1"] or counter["0"] < counter["1"]:
        comparison = "0"
    else:
        comparison = "1"
    for j in range(0, len(co2List[i])):
        if co2List[i][j] != comparison:
            for k in range(0, len(co2List)):
                co2List[k][j] = ""
    
        

oxGen = ""
co2 = ""

for i in range(0, len(co2List)):
    if "1" in set(gammaList[i]):
        oxGen += "1"
    else:
        oxGen += "0"
    if "1" in set(co2List[i]):
        co2 += "1"
    else:
        co2 += "0"
print(oxGen, co2)
result2 = int(oxGen, 2)*int(co2, 2)
print(result2)