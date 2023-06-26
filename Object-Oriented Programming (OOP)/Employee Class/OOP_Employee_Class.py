#By Alexandros Panagiotakopoulos - alexandrospanag.github.io
# employee example
class Employee():
   #class that defines the employee on a company
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# main program
the_employees = []
while True:
    name = input('Enter the employee name:')
    if not name: break
    salary = input('Enter the employee salaryς:')
    the_employees.append(Employee(name, salary))

# print the employees
for employee in the_employees:
    print(employee.name, employee.salary, sep='\t')