n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# print("hi")
"""
*
**
***
****
"""
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
   *
  **
 ***
****
 """
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()
