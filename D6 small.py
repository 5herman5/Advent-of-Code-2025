import math
f = open("inp.txt", "r")
s = f.read()

l = [[i for i in line.split() if i != ""] for line in s.split("\n")]
lv = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]

ops = {"+": sum, "*": math.prod}
t = sum(ops[col[-1]](int(i) for i in col[:-1]) for col in lv)
print(t)

l = [line for line in s.split("\n")]
ls = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
indices = [i for i, a in enumerate(ls) if a[-1] in "+*"] + [len(ls)]
sections = [(indices[i], indices[i+1]) for i in range(len(indices) - 1)]

t = sum(ops[ls[a][-1]](int("".join(ls[i][:-1])) for i in range(a, b) if len(set(ls[i])) > 1) for a, b in sections)
print(t)