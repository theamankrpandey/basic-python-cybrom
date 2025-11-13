a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a==b==c==a:
    print("equilateral triangle")
elif a==b or c==b or b==a or b==c:
        print("two sides are equal")
else:
    print("all side are different")