#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

class PartyAnimal:
    x=0
    name=""
    def __init__(self, nam):
        self.name=nam
        print(self.name,"constructed")

    def party(self):
        self.x = self.x+1
        print(self.name,"drank",self.x,"shots")

#the class pizzaeater inherits the partyanimal classes and extends them
class PizzaEater(PartyAnimal):
    points=0
    def touchdown(self):
        self.points = self.points+7
        self.party()
        print(self.name,"ate",self.points,"pizzas")

s = PartyAnimal("Sally")
s.party()


j = PizzaEater("Jim")
j.party()
j.touchdown()