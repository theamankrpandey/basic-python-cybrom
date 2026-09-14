a = [4, 8, 6, 7, 3]
target = 7
d = {}
for i in a:
    require = target - i
    if require in d:
        print("i:-", require, "j:-", i)
        break
    d[i] = i