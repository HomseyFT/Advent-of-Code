import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://adventofcode.com/2025/day/1/input"
session = os.getenv("SESSION")
num = 50
count = 0
response = requests.get(url, stream = True, cookies = {"session": session})

for rline in response.iter_lines():
    if rline:
        line = rline.decode().strip()
        r = int(line[1:])
        if line[0] == "R":
            if num == 0:
                k = 100
            else:
                k = 100 - num
            if r >= k:
                count += 1 + (r - k) // 100
            num = (num + r) % 100
        else:
            if num == 0:
                k = 100
            else:
                k = num
            if r >= k:
                count += 1 + (r - k) // 100
            num = (num - r) % 100

print(count)


    



