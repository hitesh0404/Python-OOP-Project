from vehicle import Car
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Society:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Human(Animal,Society):

    def __init__(self, name, age, species,society_name, location):
        Animal.__init__(self, name, age, species)
        Society.__init__(self,society_name,location)

class Person(Human):
    persons = []
    def __init__(self, name, age, species, society_name, location,net_worth):
        super().__init__(name=name, age=age, species=species, society_name=society_name, location=location)
        self.net_worth = net_worth
        self.cars=[]
        Person.persons.append(self)
        
    def buy_car(self,make, model, year, engine_size, num_doors,seats):
        self.cars.append(Car(make, model, year, engine_size, num_doors,seats))
    def sell_car(self,car):
        self.cars.remove(car)



