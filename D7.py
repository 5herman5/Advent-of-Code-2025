f = open("inp.txt", "r")
s = f.read()

l = [line for line in s.split("\n")]

_splits = set()
_dict2 = {}

def timelines(n, l, x):
    if (n, x) not in _dict2:
        if n == len(l):
            _dict2[n, x] = 1
        elif l[n][x] == ".":
            _dict2[n, x] = timelines(n+1, l, x)
        else:
            _dict2[n, x] = timelines(n+1, l, x-1) + timelines(n+1, l, x+1)
            _splits.add((n, x))

    return _dict2[n, x]

print(timelines(1, l, l[0].find("S")), len(_splits))