import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://adventofcode.com/2025/day/4/input"
session = os.getenv("SESSION")
response = requests.get(url, stream = True, cookies = {"session": session})

count = 0
grid = []

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),]

for rline in response.iter_lines():
    line = rline.decode().strip()
    grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

while True:
    toRemove = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                neighbors = 0
                for dr, dc in dirs:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        if grid[rr][cc] == '@':
                            neighbors += 1
                if neighbors < 4:
                    toRemove.append((r,c))
    if not toRemove:
        break

    for r,c in toRemove:
        grid[r][c] = '.'
    count += len(toRemove)

print(count)
