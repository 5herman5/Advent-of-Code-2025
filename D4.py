f = open("inp.txt", "r")
s = f.read()

l = [list(line) for line in s.split("\n")]
t = 0

for j, row in enumerate(l):
    for i, v in enumerate(row):
        n = 0
        if v != "@":
            continue
        possible = [(i + a, j + b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        for x, y in possible:
            if y >= 0 and y < len(l) and x >= 0 and x < len(row):
                n += (l[y][x] == "@")
        
        t += (n < 5)

print(t)

changes = {1}
t = 0

while len(changes) > 0:
    changes = set()
    for j, row in enumerate(l):
        for i, v in enumerate(row):
            n = 0
            if v != "@":
                continue
            possible = [(i + a, j + b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
            for x, y in possible:
                if y >= 0 and y < len(l) and x >= 0 and x < len(row):
                    n += (l[y][x] == "@")
            
            if (n < 5):
                t += 1
                changes.add((i, j))
    
    for (i, j) in changes:
        l[j][i] = "."

print(t)