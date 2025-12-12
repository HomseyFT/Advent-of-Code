import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://adventofcode.com/2025/day/5/input"
session = os.getenv("SESSION")
response = requests.get(url, stream = True, cookies = {"session": session})

ranges = []
ids = []
count = 0

for rline in response.iter_lines():
    line = rline.decode().strip()
    if "-" in line:
        ranges.append(line.split("-"))
    elif line != "":
        ids.append(line)

for x in ids:
    n = int(x)
    fresh = False
    for i in range(len(ranges)):
        elem1 = ranges[i][0]
        elem2 = ranges[i][1]
        if n >= int(elem1) and n <= int(elem2):
            count += 1
            fresh = True
        if fresh:
            break

print(count)
