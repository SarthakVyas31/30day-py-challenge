class Factorial:
    def fact(self,n):
        if n == 0 or n == 1:
            return 1
        return n*self.fact(n-1)
    

number = int(input("Enter number for it's factorial: "))
F = Factorial()
print(f"{number}! = {F.fact(number)}")
