mylist = ["Element1","Element2","Element3"]
for i in range(len(mylist)):
    print(mylist[i])  #this command prints each element on the list however, Python doesn't require that method
#and it's a common mistake that beginners are making or people that come from different programming languages
#by default, python can utilize this command better:

for i in mylist:
    print(i)