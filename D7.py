f = open("inp.txt", "r")
s = f.read()

l = [line for line in s.split("\n")]

_splits = set()
_timelines = {}

def timelines(n, l, x):
    if (n, x) not in _timelines:
        if n == len(l):
            _timelines[n, x] = 1
        elif l[n][x] == ".":
            _timelines[n, x] = timelines(n+1, l, x)
        else:
            _timelines[n, x] = timelines(n+1, l, x-1) + timelines(n+1, l, x+1)
            _splits.add((n, x))

    return _timelines[n, x]

print(timelines(1, l, l[0].find("S")), len(_splits))