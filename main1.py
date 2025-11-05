def decoratoro(x):
    def hello():
        print("teansaction initiated")
        x()
        print("transaction succesful")
    return hello
@decoratoro
def hii():
    print("excuating all steps")
hii()