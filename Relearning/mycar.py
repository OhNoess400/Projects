from car import Car,ElectricCar,Battery
from random import randint

my_new_car= Car('audi','a4',2016)
print(my_new_car.describe())

my_new_ECar= ElectricCar("tesla","roadster",2017)
print(my_new_ECar.describe())
my_new_ECar.battery.get_range()

x=randint(1,6)
print(x)
