class Dog():
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def sit(self):
        print(self.name.title(), "is now sitting.")

    def roll_over(self):
        print(self.name.title(), "has rolled over!")

my_dog=Dog("Jeff",9)
print("My dog's name is",my_dog.name.title()+".")
print("My dog is",str(my_dog.age),"years old.")
my_dog.sit()
my_dog.roll_over()

class Shop():
    def __init__(self,shop_Name,cuisine_Type):
        self.shop_Name= shop_Name
        self.cuisine_Type= cuisine_Type

    def describe_shop(self):
        print("The shop's Name is",self.shop_Name.title()+".")
        print("The shop serves",self.cuisine_Type.title()+".")
    def open_shop(self):
        print("The restruant is now open")

shop1=Shop("Everest","Nepali")
print(shop1.shop_Name.title())
shop1.describe_shop()
shop1.open_shop()




class User():
    def __init__(self,firstName,lastName,location,username):
        self.First_Name= firstName
        self.Last_Name= lastName
        self.Location= location
        self.Username=username
    def User_Info(self):
        print("\nUser Info for",self.Username+":",
        "\nFirst Name:\n-",self.First_Name,
        "\nLast Name:\n-",self.Last_Name,
        "\nLocation:\n-",self.Location)
    def Greet_User(self):
        print("Hello,",self.Username,
        "what is the weather like in",self.Location.title()+"?\n")

User1=User("Jake","Baldino","Toronto","JBald")
User1.User_Info()
User1.Greet_User()
User2=User("James","Grimaldis","Cary","Grimaldisio")
User2.User_Info()
User2.Greet_User()

class SmallerDog(Dog):
    def __init__(self, name, age):
        super().__init__(name,age)

newdog=SmallerDog("Wille",12)
newdog.sit()

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

myElectric=ElectricCar("Tesla","Model S",2016)
print(myElectric.describe())
myElectric.battery.describe_Battery()
myElectric.fill_tank_gas()
myElectric.battery.get_range()
