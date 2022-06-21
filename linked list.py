#Linked list is a collection of objects called nodes that are randomly stored in the memory.
#A node contains two fields i.e. data stored at that particular address and the pointer which contains the address of the next node in the memory.
#The last node of the list contains pointer to the null.

class Node:
    def __init__(self, v = None):
        self.v = v
        self.next = None
             
class Linkedlist:
    def __init__(self):
        self.head = None
             
    #traversing
    def traverse(self):
        n = self.head
        while n!=None:
            print(n.v,end=" ")
            n = n.next
   
    #add new node at beginning
    def add_at_begin(self,v):
        self.v = v
        newn = Node(self.v)
        newn.next = self.head
        self.head = newn
             
    #add new node at end
    def add_at_end(self,v):
        self.v = v
        newn = Node(self.v)
             
        if self.head == None:
            self.head = newn
            return
             
        lastn = self.head
        while lastn.next:
            lastn = lastn.next 
        lastn.next = newn
             
    #add new node in between the nodes
    def add_in_betw(self,aftern,v):
        self.aftern = aftern
        self.v = v
             
        if self.aftern.next == None:
            print("Node does not exist")
            return
             
        newn = Node(self.v)
        newn.next = self.aftern.next
        self.aftern.next = newn
             
    #Delete a node
    def dele(self,v):
        self.v = v
        temp = self.head
             
        if temp!=None:
            if temp.v == self.v:
                self.head = temp.next
                temp = None
                     
        while temp!=None:
            if temp.v == self.v:
                break
            ptr = temp
            temp = temp.next
                 
        if temp == None:
            print("Node does not exist")
            return
             
        ptr.next = temp.next
        temp = None
             
    #reverse the linked list
    def rev(self):
        prev = None
        cur = self.head
        next = None
             
        while cur!=None:
            next = cur.next
            cur.next = prev
                 
            prev = cur
            cur = next
                 
        self.head = prev
             
             
                    
obj = Linkedlist()
obj.head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
obj.head.next = n2
n2.next = n3
n3.next = n4
obj.add_at_begin(5)
obj.add_at_end(6)
obj.add_in_betw(obj.head.next, 8)
obj.dele(8)
print("created linked list: ",end = " ")
obj.traverse()
obj.rev()
print("\n-------------------------------")
print("after reversing: ",end = " ")
obj.traverse()

