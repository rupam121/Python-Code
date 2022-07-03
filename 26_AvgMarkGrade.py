

phy = int(input('enter phy mark: '))
chem = int(input('enter chem mark: '))
math = int(input('enter math mark: '))
bio = int(input('enter bio mark: '))
it = int(input('enter it mark: '))
eng = int(input('enter eng mark: '))

total = phy+chem+math+bio+it+eng

avgmark = total/6

print(total)
print(avgmark)

if avgmark >= 90:
    print(' o grade ')
elif avgmark >= 80 and avgmark <= 89:
    print(' e grade ')
elif avgmark >= 70 and avgmark <= 79:
    print(' a grade ')
elif avgmark >= 60 and avgmark <= 69:
    print(' b grade ')
elif avgmark >= 50 and avgmark <= 59:
    print(' c grade ')
else:
    print(' failed ')
