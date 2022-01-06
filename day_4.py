from get_input import *

url = "https://adventofcode.com/2021/day/4/input"

text = get_input(url)[0]

randomNumbers = text.split("\n")[0].split(",")

print(randomNumbers)