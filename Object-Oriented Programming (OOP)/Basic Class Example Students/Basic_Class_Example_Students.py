#self refers to each object that will be created
class Student:
	#creating a class that contains students that are studying
	#each student has their own name, age, origin 
    def __init__(self,name,age,origin='',phone=''):
	    self.name=name 
	    self.age=age
	    self.origin=origin
	    self.phone=phone
	    
    def get_age(self):
	    return str(self.age)+' years old'
	
    def get_phone(self):
	    return str(self.phone)+' is the phone number of '+str(self.name) 

#creating multiple objects from the class
s1 = Student('Alex', 22, 'Volos', 'XXX-YYY-ZZZZ') #creating a student
s2 = Student('Marios', 23, 'Thessaloniki', 'ZZZ-YYY-XXXX') #creating another student with different attributes

print(s1.name) #get the s1 name (Alex)
print(s1.get_age()) #get the s1 age (Alex) by calling the function inside the class
print(s2.get_phone()) #get the s2 phone and name by calling the get_phone function