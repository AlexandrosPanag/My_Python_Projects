# By Alexandros Panagiotakopoulos - alexandrospanag.github.io

reply = " "

while reply != "stop":
    x,y=" ", " "
    while type(x) is str or type(y) is str:
        try:
            x = int (input("x=").strip())
            y = int (input("y:").strip())
            print("x/y = {}, x%y = {}".format(x/y, x%y))
        except ValueError as e:
            print("Give an integer number:",e)
        except ZeroDivisionError as e:
            print("Warning: no division with 0\n",e)
        finally:
            reply = input("Type stop for exit")
            if reply == "stop":
                break
