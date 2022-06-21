#A stack is a linear data structure where data is arranged objects on over another.
#It stores the data in LIFO (Last in First Out) manner.
#We can perform the two operations in the stack - PUSH and POP.
#The PUSH operation is when we add an element and the POP operation is when we remove an element from the stack.

class stack:
    def __init__(self):
        self.stack = []
        
    def add(self,v):
        self.v = v
        self.stack.append(self.v)
        
    def rem(self):
        if len(self.stack)<=0:
            print("Stack is empty")
        else:
            self.stack.pop()
            
    def disply(self):
        print(self.stack)
            
    def displaytop(self):
        print(self.stack[-1])
        
obj = stack()
obj.add(1)
obj.add(2)
obj.rem()
obj.disply()
obj.displaytop()
