num_list=[]

def Input():
    n=int(input("How many numbers do you want in your list: "))
    for i in range(n):
        value=int(input(f"Enter number {i+1}:"))
        num_list.append(value)
    print("Your list is :",num_list)
    return n

def Sum():
    Total=sum(num_list)
    print(f"Sum of your number list: {Total}")
    return Total

def Average(Total,n):
    if n ==0:
        print("Cannot divide by zero")
        return
    Avg = Total/n
    print(f"Average of your number list is: {Avg}")

n=Input()
total=Sum()
Average(total,n)