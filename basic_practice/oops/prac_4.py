# create a class pets from animals and further create a class dog pets
# add a method bark in dog class

class Animals:
    # some functions
    pass

class Pets(Animals):
    # some functions
    pass

class Dog(Pets):
    def bark(self):
        print("BOW BOW")

d=Dog()
d.bark()