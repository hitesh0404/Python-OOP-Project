class Vehicle:
    """
    this is doc string which describe the essential things
    about the vehicle class 
    """
    def __init__(self, make, model, year):
        """
        this is doc string inside the Method
        """
        self.make = make
        self.model = model
        self.year = year

class TransportVehicle(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

class LightMotorVehicle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

class Car(LightMotorVehicle):
    def __init__(self, make, model, year, engine_size, num_doors,seats):
        super().__init__(make, model, year, engine_size)
        self.num_doors = num_doors
        self.seats = seats

class Truck(TransportVehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year, capacity)





    
