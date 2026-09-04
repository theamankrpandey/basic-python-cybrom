a = int(input("enter number"))
rev=0
n = a
while n >0:
    digit = n %10
    rev = rev * 10  +digit
    n = n//10
if a == rev :
    print("true")
else:
    print("False")