#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

class Lifecycle:
    x = 0
    name = ''
    def __init__(self, nam): #constructor example
        self.name = nam
        print(self.name,'constructed')
    def party(self): #objects constructed counter example
        self.x = self.x + 1
        print(self.name,'total counter',self.x)
    
    #def __del___(self): //optional code for destructor 
       #print("I am destructed", self.x)

a = Lifecycle('Object1')
b = Lifecycle('Object2')

a.party()
b.party()
a.party()