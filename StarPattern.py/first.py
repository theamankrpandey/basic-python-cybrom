# 🔥 TOP 8 — Priority Order
# 1. Square ⭐⭐⭐⭐⭐
# * * * *
# * * * *
# * * * *
# * * * *

# Formula: हर row में n stars

# n = 4

# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()
# 2. Increasing Triangle ⭐⭐⭐⭐⭐
# *
# * *
# * * *
# * * * *

# Formula: stars = i

# n = 4

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# 3. Decreasing Triangle ⭐⭐⭐⭐⭐
# * * * *
# * * *
# * *
# *

# Formula: stars = n-i+1

# n = 4

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# 4. Number Triangle ⭐⭐⭐⭐⭐
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# n = 4

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# बस * की जगह j print कर दिया.

# 5. Same Number Triangle ⭐⭐⭐⭐
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# n = 4

# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# Logic: row number i ही print होगा।

# 6. Pyramid ⭐⭐⭐⭐⭐
#    *
#   * *
#  * * *
# * * * *

# सबसे important formula:

# Spaces = n-i

# Stars = i (जब "* " print कर रहे हो)

# n = 4

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
    
#     for j in range(i):
#         print("*", end=" ")
    
#     print()
# 7. Inverted Pyramid ⭐⭐⭐⭐
# * * * *
#  * * *
#   * *
#    *
# n = 4

# for i in range(n, 0, -1):
#     print(" " * (n-i), end="")
    
#     for j in range(i):
#         print("*", end=" ")
    
#     print()
# 8. Diamond ⭐⭐⭐⭐⭐
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

# Isko 2 patterns combine karke bana:

# n = 4

# # Upper
# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # Lower
# for i in range(n-1, 0, -1):
#     print(" " * (n-i), end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()