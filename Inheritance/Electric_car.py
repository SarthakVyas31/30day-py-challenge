from car import Car

class ElectricCar(Car):
    def __init__(self,make="",model="",year=0,color="",battery_capacity=""):
        super().__init__(make,model,year,color)
        self.battery_capacity = battery_capacity
    
    def get_input(self):
        self.make = input("Enter Make of your car: ")
        self.model = input("Enter Model of your car: ")
        self.year = int(input("Enter Purchase Year of your car: "))
        self.color = input("Enter Color of your car: ")
        self.battery_capacity = input("Enter Battery capacity:")

    def display(self):
        print("\n-----------Printing Car Details-----------\n")
        print("Make of Car:", self.make)
        print("Model of Car:", self.model)
        print("Purchase year of Car:", self.year)
        print("Color of Car:", self.color)
        print("Battery Capacity of Car:", self.battery_capacity , "kwh")

Ev_1=ElectricCar()

Ev_1.get_input()
Ev_1.display()
print("\n")
Ev_1.Drive()
Ev_1.Stop()
print("\n")