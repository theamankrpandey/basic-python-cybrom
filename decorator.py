def outer(x):
    def inner():
        print("welcome")
        x()
    return inner
def display():
    print("hello")
res=outer(display)
res()