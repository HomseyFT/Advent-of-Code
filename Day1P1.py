import requests

url = "https://adventofcode.com/2025/day/1/input"
session = "53616c7465645f5f9c542392b4a5bbe40f6c0981f2da44e717174d63b35beadd5954a512fcba5a95a00027216fa7e0cefbc116ad90c4bc6bdb508ed9259775d5"
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


    



