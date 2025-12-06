f = open("inp.txt", "r")
s = f.read()

l = [[i for i in line.split() if i != ""] for line in s.split("\n")]
lv = [[row[i] for row in l] for i in range(len(l[0]))]

t = 0
for col in lv:
    operator = col[-1]
    if operator == "+":
        t += sum(int(i) for i in col[:-1])
    else:
        p = 1
        for i in col[:-1]:
            p *= int(i)
        t += p

print(t)

l = [line for line in s.split("\n")]
ls = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
indices = [i for i, a in enumerate(ls) if a[-1] in "+*"]

t = 0
p = 0
c = 0
for i in range(len(l[0])):
    if i in indices:
        t += p
        p = (ls[i][-1] == "*")
        c = p
    if len(set(ls[i])) == 1:
        continue
    if c == 1:
        p *= int("".join(ls[i][:-1]))
    else:
        p += int("".join(ls[i][:-1]))

t += p
print(t)