# WHAT IS REQUIREMENT OF CONDITIONAL STATEMENT ?
# TYPES ARE: IF , IF ELSE , IF ELIF ELSE.


# input student mark and check the result
# pass or fail
# mark>=33 pass fail


# mark = int(input('enter your mark : '))
# if mark >= 33:
#     print('congratulation u pass')

# if mark <= 33: #again check the condition
#     print('sorry u failed')


# IF ELSE

# mark = int(input('enter ur mark : '))

# if mark >= 33:
#     print('Cong.. u pass')

# else:  # not required to check any condition
#     print('sry fail')


# IF ELIF ELSE

num = int(input('enter a number btn 1-5 : '))

if num == 1:
    print('a')
elif num == 2:
    print('b')
elif num == 3:
    print('c')
elif num == 4:
    print('d')
elif num == 5:
    print('e')
else:
    print('invalid option plz choose valid option')
