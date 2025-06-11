#Create a decorator to log function execution time
import time 

def log(func):
    def wrapper(*args , **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} function executed in {duration} sec")
        return result  
    return wrapper


def Factorial(a):
    if a<2:
        return 1
    return Factorial(a-1)*a

@log
def output(a):
    return Factorial(a)

n = int(input("enter number:"))
print(output(n))