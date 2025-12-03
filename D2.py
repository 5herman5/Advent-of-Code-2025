f = open("inp.txt", "r")
s = f.read()

l = [(int(line.split("-")[0]), int(line.split("-")[1])) for a in s.split("\n") for line in a.split(",")]

c = 0
for a, b in l:
    for i in range(a, b+1):
        k = str(i)
        for n in range(1, len(k)):
            if len(k) % n == 0:
                v = set([k[n * ind : n * (ind + 1)] for ind in range(len(k) // n)])
                if len(v) == 1:
                    c += i
                    break

print(c)