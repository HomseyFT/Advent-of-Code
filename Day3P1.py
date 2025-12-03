import requests

url = "https://adventofcode.com/2025/day/3/input"
session = "53616c7465645f5f9c542392b4a5bbe40f6c0981f2da44e717174d63b35beadd5954a512fcba5a95a00027216fa7e0cefbc116ad90c4bc6bdb508ed9259775d5"
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





    
    



