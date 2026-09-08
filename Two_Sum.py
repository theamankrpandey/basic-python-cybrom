a = [4, 8, 6, 7, 3]
target = 7
d = {}
for i in range(len(a)):

    x = target - a[i]

    if x in d:
        print("i:-", d[x], "j:-", i)

    d[a[i]] = i