#A queue is a linear type of data structure used to store the data in a sequentially.
#The concept of queue is based on the FIFO, which means "First in First Out".
#The queue has the two ends front and rear.
#The next element is inserted from the rear end and removed from the front end.

class queue:
    def __init__(self):
        self.queue = []
         
    #add an element
    def add(self,v):
        self.v = v
        self.queue.insert(0,self.v)
         
    #remove an element
    def rem(self):
        if len(self.queue)<=0:
            print("Queue is empty")
        else:
            self.queue.pop()
         
    #print queue
    def display(self):
        print(self.queue)
         
    #print front of the queue
    def displayFront(self):
        print(self.queue[0])
         
obj = queue()
obj.add(1)
obj.add(2)
obj.add(5)
obj.add(6)
obj.add(9)
obj.add(20)
obj.rem()
obj.display()
obj.displayFront()
