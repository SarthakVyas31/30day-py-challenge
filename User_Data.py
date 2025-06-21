#Build a Pydantic model for a user profile with fields for name, email, and age, including validation for email 
# format and age range (18–100)

from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value <=18:
            raise ValueError(f"age must be above 18 years")
        elif value >=100:
            raise ValueError(f"age must be below 100 year")
        return value 
    
    def Display_Json(self):
        print(self.model_dump_json(indent = 4))
    

def User_Input():
    User_name = input("Enter your Name: ")

    while True:
        try:  
            User_age = int(input("Enter your Age: "))
            break
        except ValueError:
            print("enter valid integer for age.")

    User_email = input("Enter your Email Id: ")
    return User(name = User_name, age = User_age, email = User_email)

def Run():
    users = []
    while True:
        user = User_Input()
        users.append(user)

        multiple = input("Do you want to add another User data?(Yes/No): ")

        if multiple!= "Yes":
            break
    
    

    for index, user in enumerate( users, 1):
        print(f"\nUser Data {index}:\n")
        user.Display_Json()

if __name__ == "__main__":
    Run()