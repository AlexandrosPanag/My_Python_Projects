
mo = input("Give the amount of money:")
interest = input("Give the interest per year:")
totalvalue=0
yearselapsed=0
while totalvalue<1000000:
    totalvalue+=int(mo)*(int(interest)/100)
    yearselapsed+=1
print("Total years that will be required in order to become a millionaire:",yearselapsed)
