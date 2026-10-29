#Parent/Super/Base Class
class Animal:

    isMammal = True
    gender = "Male"
    age = 2

    def movement(self):
        print("Animal is moving")

#Child/SubDerived Class
class Cow(Animal):
    def moow(self):
        print("Cow is moowing")



class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

myCow = Cow()
myCow.moow()

myCat = Cat()
myCat.meow()