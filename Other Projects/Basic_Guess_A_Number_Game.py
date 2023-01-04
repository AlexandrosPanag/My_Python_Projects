# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

list = [1,33,67,89,24,12,124,93]
userinput = int(input("Guess a number from the list: "))
for i in list:
    if i == userinput:
        print("You guessed correctly, you found a number!")
        break
    else:
        print("Wrong guess!")
