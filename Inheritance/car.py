class Car:
    def __init__(self , make ,model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def Drive(self):
        print("This " + self.model+ " is driving")

    def Stop(self):
        print("This " + self.model + " is stopped")
    