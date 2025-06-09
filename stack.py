class Stack:
    def __init__(self):
        self.container = []
    
    def push(self, container):
        self.container.append(container)
    
    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return "Underflow(Stack is empty)"
    
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Stack is empty"
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return f"Stack: {list(reversed(self.container))}"

stk = Stack()
n = int(input("Enter the size of stack:"))

for i in range(n):
    x=int(input(f"Enter the value for {i} element: "))
    stk.push(x)

print(stk)
print(f"Top element of Stack is {stk.peek()}")

p = stk.pop()
print(f"Pop the element from Stack: {p}")
print(stk)

print(f"Size of Stack: {stk.size()}")
print(f"Is Stack empty: {stk.is_empty()}")