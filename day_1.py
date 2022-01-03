from math import inf
from get_input import *

url = "https://adventofcode.com/2021/day/1/input"
depths = []

text = get_input(url)

for i in text:
    temp = i

depths = temp.split("\n")
depths.pop()
depths = list(map(int, depths))

count = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        count += 1
        
print(count)

newCount = 0
previous = inf
depthGroup = 0
for i in range(2, len(depths)):
    depthGroup = sum(depths[i - 2 : i + 1])
    if depthGroup > previous:
        newCount += 1
    previous = depthGroup

print(newCount)
