num=" "
while type(num) is str:
    num = input("Give a number:")
    try:
        num=float(num)
    except ValueError:
        print("Please give a number")
print("Thank you for the input")