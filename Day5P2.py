import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://adventofcode.com/2025/day/5/input"
session = os.getenv("SESSION")
response = requests.get(url, stream = True, cookies = {"session": session})

intervals = []
merged = []


for rline in response.iter_lines():
    line = rline.decode().strip()
    if "-" in line:
        a,b = line.split("-")
        intervals.append((int(a), int(b)))

intervals = sorted(intervals)

for start,end in intervals:
    if not merged:
        merged.append([start, end])
    else:
        lastStart, lastEnd = merged[-1]
        if start > lastEnd:
            merged.append([start, end])
        else:
            merged[-1][1] = max(lastEnd, end)

total = sum(end - start + 1 for start, end in merged)
print(total)


    



