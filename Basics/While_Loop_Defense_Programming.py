# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

num = 0
while num > 99 or num <10:
    num = int(input("Give a positive double digit number"))
else:
    print("thank you, you gave {:2d}".format(num))
