def isnum(n):
# function that checks if a string is a number
    if not type(n) is str:
        return False
    n= n.strip()
    if n.isdigit():
        return True   
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".")==1 and isnum(n.replace(".","")):
          return True
        else:
            return False
    else:
        return False
while True:
    n=input("n=")
    if n=='':break
    print(isnum(n))