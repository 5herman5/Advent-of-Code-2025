f = open("inp.txt", "r")
s = f.read()

l = [line for line in s.split("\n")]

for part in (2, 12):
    t = 0
    
    for row in l:
        ns = [-1]
        for i in list(range(part))[::-1]:
            section = row[:-i] if i != 0 else row
            ns.append(min(n for n, a in enumerate(section) if a == max(b for n2, b in enumerate(section) if n2 > max(ns)) and n > max(ns)))
        t += sum(int(row[i]) * (10**n) for n, i in enumerate(ns[1:][::-1]))

    print(t)