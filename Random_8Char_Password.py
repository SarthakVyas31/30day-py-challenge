import random as r
import string as str

def random_password():
    Password_length=8
    String= str.ascii_letters+str.punctuation

    password=""
    for i in range(Password_length):
        password+=r.choice(String)


    return password

print("Your random 8-bit character password is:",random_password())

