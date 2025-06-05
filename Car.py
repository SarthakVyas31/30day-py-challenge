class Car:
    def __init__(self , brand_name , car_model , Year , car_color):
        self.brand = brand_name
        self.model = car_model
        self.year = Year
        self.colour = car_color
    
    def car(self):
        print("\nPrinting Car Details:\n")
        print(f" Car Brand: {self.brand}\n Car Model: {self.model} \n Year: {self.year}\n Car Colour: {self.colour}")


name= input("Enter your car brand name:")
model= input("Enter your car model:")
year = input("Enter purchase year:")
colour = input("Enter your car colour:")

details = Car(name , model , year , colour)
details.car()