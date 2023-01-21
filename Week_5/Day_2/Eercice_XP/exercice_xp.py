"""#Exercice 1 Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
            for animal in self.animals:
                print(animal.walk())


class Cat():
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class  Siamese(Cat):
    def __init__(self, name, age, sounds):
        Cat.__init__(self, name, age)
        self.sounds=sounds
        
        
bengal1=Bengal("Mouss",2)
Chartreux1=Chartreux("Boo",3)
Siamese1=Siamese("Milou",5,"Miole")
all_cats=[bengal1,Chartreux1,Siamese1]
#print(all_cats[0].name,all_cats[1].name,all_cats[2].age)

Sara_pets=Pets(all_cats)
#print(Sara_pets.animals[0].name)
Sara_pets.walk()

"""
#Exercice 2 : Dogs 

class Dog():
    def __init__(self,name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self,other_dog):
        if self.run_speed()>other_dog.run_speed():
            print(f"{self.name} is winner !")
        elif self.run_speed()<other_dog.run_speed():
            print(f"{other_dog.name} is winner !")
        else:
            print("Match NULL !")


"""dog1=Dog("Boby",4,31)
dog2=Dog("Blacky",4,31)
dog3=Dog("Patience",5,27)
dog1.fight(dog2)
dog2.fight(dog3)
dog1.fight(dog3)"""


"""print(dog1.bark())
print(dog1.run_speed())
print("=======================================")
print(dog2.bark())
print(dog2.run_speed())"""


#Exercice 3 : Dogs Domesticated



