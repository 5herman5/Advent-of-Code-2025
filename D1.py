f = open("inp.txt", "r")
s = f.read()

l = [(int(row[1:]) * (-1 if row[0] == 'L' else 1)) for row in s.split("\n")]

n = 50
c2 = 0
c1 = 0

for v in l:
    np = n
    n += v
    nm = n
    n %= 100
    c1 += (n == 0)
    c2 += abs(nm // 100) + (n == 0 and nm <= 0) - (np == 0 and nm < 0)

print(c1, c2)