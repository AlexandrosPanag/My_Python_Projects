#alexandrospanag.github.io - Alexandros Panagiotakopoulos 2023

class My_class():
    def __init__(self):
        self.publ= "i am a public attribute" #declare a public attribute (instance/element)
        self.__priv="i am a private attribute" #declare a private attribute

    def get_priv(self): #function to get the private element
        return self.__priv
    
t = My_class()
print(t.publ) #print the public element
print(t.get_priv()) #function that prins the private element
# print(t.__priv) -- notice how it is not allowed to be printed!!!!