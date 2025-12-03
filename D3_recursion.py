f = open("inp.txt", "r")
s = f.read()

l = [line for line in s.split("\n")]

def get_max(row, n):
    if n == 0:
        return max(row)
    section = row[:-n]
    val = max(section)
    cut = min(i for i, a in enumerate(section) if a == val)
    return get_max(row[cut+1:], n - 1) + val

total1 = sum(int(get_max(row, 1)[::-1]) for row in l)
total2 = sum(int(get_max(row, 11)[::-1]) for row in l)

print(total1, total2)