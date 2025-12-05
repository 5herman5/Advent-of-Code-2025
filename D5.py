f = open("inp.txt", "r")
s = f.read()

top, bottom = s.split("\n\n")

rules = [(int(row.split("-")[0]), int(row.split("-")[1])) for row in top.split("\n")]

print(len([1 for num in bottom.split("\n") if any(int(num) >= a and int(num) <= b for a, b in rules)]))

vals = []

for a, b in rules:
    vals.append((a, 1))
    vals.append((b + 1, -1))

vals.sort(key = lambda x: x[0])

c = 0
prev = 0
n = 0

for a, b in vals:
    if c > 0:
        n += a - prev
    prev = a
    c += b

print(n)