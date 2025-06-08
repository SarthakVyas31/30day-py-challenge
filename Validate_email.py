import re

class Validate:
    def User_input(self):
        self.First_name = input("Enter your First name: ") 
        self.Last_name = input("Enter your Last name: ")
        self.Email = input("Enter your valid Email: ")

    def Verify(self):
        pattern = r"[A-Za-z0-9]+@[a-zA-z]+\.(com|in|org)"
        return re.fullmatch(pattern, self.Email)
           
        
    def Display(self):
        print("\n --------Printing Details--------\n")
        print("Your name:", self.First_name+" "+self.Last_name)
        print("Your Email: ", self.Email)

Check = Validate()
Check.User_input()

if Check.Verify():
 print("Valid Email")  
 Check.Display()    
else:
  print("Ivalid Valid Email")
