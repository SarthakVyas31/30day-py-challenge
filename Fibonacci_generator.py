#Generate the first n Fibonacci numbers with a generator
class Fibonacci:
    def Input(self):
        self.start = int(input("Enter starting number:"))
        self.stop = int(input("Enter ending number:"))

    def Generator(self , start ,stop):
        a, b = 0, 1
        while a <= self.stop:
            if a >= self.start:
                yield a
            a, b = b, a + b
    
    def Display(self):
        Fib_List = list(self.Generator(self.start, self.stop))
        print(Fib_List)


Fib_Gen = Fibonacci()
Fib_Gen.Input()
Fib_Gen.Display()
