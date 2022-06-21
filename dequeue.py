#A Deque, also known as a Double-ended queue, has the attribute of inserting and deleting data elements from either end.
#The deque module is a segment of the library known as collections.
#It contains the attributes to add and remove data elements that can be invoked directly with parameters.
#In order to declare a deque, we have to import the collections library first.

import collections

class dequeue:
    def __init__(self, l):
        self.l = l
        self.dq = collections.deque(self.l)
        
    def addleft(self, v):
        self.v = v
        self.dq.appendleft(self.v)
        
    def addright(self, v):
        self.v = v
        self.dq.append(self.v)
        
    def delright(self):
        if len(self.dq)<=0:
            print("Dequeue is empty")
        else:
            self.dq.pop()
        
    def delleft(self):
        if len(self.dq)<=0:
            print("Dequeue is empty")
        else:
            self.dq.popleft()
        
    def display(self):
        print(self.dq)

l = [2,1,4,5]
obj = dequeue(l)
obj.addleft(1)
obj.addleft(2)
obj.addright(3)
obj.addright(4)
obj.delleft()
obj.delright()
obj.display()
    
