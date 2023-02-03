
# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(revs_number))


# n = 123456
# print(str(n)[::-1])

# def add_i(x, y):
#     x += [1, 2]
#     y += (3, 4)


# l = [0]
# t = (5,)
# add_i(l, t)
# print(l, end="")
# print(t)

# def f_name():
#     print("hi")
# f_name()
