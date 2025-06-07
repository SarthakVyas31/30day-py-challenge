import datetime 

class Difference:
    def input(self):
        try:
            Date1 = input("Enter 1st Date (DD-MM-YYYY): ")
            self.Date_1= datetime.datetime.strptime(Date1,"%d-%m-%Y")
                
            Date2 = input("Enter 2nd Date (DD-MM-YYYY): ")
            self.Date_2 = datetime.datetime.strptime(Date2,"%d-%m-%Y")
        except ValueError:
             print("Enter valid date format (DD-MM-YYYY)")

    def cal_diff(self):
        self.Diff= abs(self.Date_1.date() - self.Date_2.date()) 
    
    def display(self):
        print("Date 1: ",self.Date_1.strftime("%d-%m-%Y"))
        print("Date 2: ",self.Date_2.strftime("%d-%m-%Y"))
        print("Difference between two dates is" , self.Diff.days , "days")


Date_obj = Difference()

Date_obj.input()
Date_obj.cal_diff()
Date_obj.display()
