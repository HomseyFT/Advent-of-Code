import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://adventofcode.com/2025/day/3/input"
session = os.getenv("SESSION")
response = requests.get(url, stream = True, cookies = {"session": session})

tot = 0

for rline in response.iter_lines():
    line = rline.decode().strip()
    digits = [int(ch) for ch in line]
    best1st = -1
    bestFull = -1
    for num in reversed(digits):
        if best1st != -1:
            value = 10 * num + best1st
            if value > bestFull:
                bestFull = value
        if num > best1st:
            best1st = num

    tot += bestFull

print(tot)





    
    



