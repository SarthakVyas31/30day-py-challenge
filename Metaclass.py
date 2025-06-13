class Custom_name_convention(type):
    def __new__(self, class_name, bases, attr):
        x={}
        for name ,value in attr.items():
            if name.startswith("__"):
                x[name] = value
            else:
                x[name.upper()] = value 
        return type(class_name, bases, x)
    
class Name(metaclass=Custom_name_convention):
    first_name = input("Enter your first name:")
    last_name =  input("Enter your last name ")

    def display(self):
        print(f"Your name: {self.FIRST_NAME} {self.LAST_NAME}")
    


N = Name()
N.DISPLAY()