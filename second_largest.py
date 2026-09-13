#  arr = [10, 20, 4, 45, 99]
# def second_largest(n):
#     if len(n)<2:
#         return
#     largest=float("-inf")
#     second=float("-inf")
#     for i in n:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             second=i
#     return second
# n=list(map(int,input("enter a number with space").split()))
# p=second_largest(n)
# print(p)



# s = [1,44,35,66,88,999]
# largest = 0
# second_largest = 0
# for i in s:
#     if i > largest:
#         second_largest = largest
#         largest = i 
#     elif i > second_largest:
#         second_largest = i
# print(second_largest)