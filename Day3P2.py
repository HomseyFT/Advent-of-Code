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
    k = 12
    length = len(digits)
    result = []
    index = 0
    for _ in range(k):
        rem = k - len(result)
        lastStart = length - rem
        bestNum = -1
        bestPos = -1
        for i in range(index, lastStart + 1):
            if digits[i] > bestNum:
                bestNum = digits[i]
                bestPos = i

        result.append(bestNum)
        index = bestPos + 1
    result = int("".join(map(str, result)))
    tot += result

print(tot)


