
#Class
class Employee:
    #values stored in variables
    def __init__(self,name,gender,position):
        self.name = name
        self.gender = gender
        self.position = position

    #behaviours/functions
    def movement(self):
        print("Employee is walking")

employee1 = Employee("Mary","Female","Developer")#creating an object
print(employee1.name)
print(employee1.gender)
print(employee1.position)
employee1.movement()


employee2 = Employee("John","Male","Admin")

employee3 = Employee("Joseph","Male","CEO")