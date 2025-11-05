def hello():
    for i in range(500):
        yield i
res=hello()
print(res)
# print(next(res))
# print(next(res))
for j in res:
    print(j)