input = "3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,753995-801224,1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,9226851880-9226945212,7337-24735,555454-591466,7777695646-7777817695,1070-2489,81504542-81618752,2584-6199,8857860-8922218,979959461-980003045,49-128,109907-161935,53514821-53703445,362278-509285,151-286,625491-681593,7715704912-7715863357,29210-60779,3287787-3395869,501-921,979760-1021259"

def prefix(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        k = pi[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k

    return pi

codes = []

for n in input.split(","):
    [num1, num2] = n.split("-")
    start = int(num1)
    end = int(num2)
    codes.append([start, end])

sum = 0

for nums in codes:
    for i in range(nums[0], nums[1] + 1):
        s = str(i)
        length = len(s)
        if length > 1:
            pi = prefix(s)
            p = length - pi[length - 1]

            if p < length and length % p == 0 and s[0] != "0":
                sum += i

print(sum)


