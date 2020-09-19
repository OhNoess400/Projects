class Car():
    """JUST A SIMPLE CAR CLASS"""
    def __init__(self,make,model,year):
        self.make= make
        self.model= model
        self.year=year
        self.odometer_reading = 0
    def describe(self):
        long_name=str(self.year)+ " " + self.make+ " "+ self.model
        return long_name.title()
    def odometer(self):
        print("This car has",str(self.odometer_reading),"miles on it")
    def update_odometer(self,milage):
        if milage>=self.odometer_reading:
            self.odometer_reading= milage
        else:
            print("You can't roll back an odometer reading!")
    def increment_odometer(self, miles):
        self.odometer_reading +=miles

class Battery():
    def __init__(self,battery_size=70):
        self.batterysize=battery_size

    def describe_Battery(self):
        print("This car has a",str(self.batterysize)+"-kWh battery")

    def get_range(self):
        if self.batterysize==70:
            range=240
        elif self.batterysize== 85:
            range= 270

        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery= Battery()
    def describe_Battery(self):
        print("This car has a",str(self.battery)+"-kWh battery")
    def fill_tank_gas(self):
        print("Electric cars don't have gas tanks!!")
