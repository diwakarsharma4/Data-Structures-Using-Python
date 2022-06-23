#In binary search tree the value of left node must be smaller than the parent node, and the value of right node must be greater than the parent node.

class Node:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.v = v
         
    #insert a node
    def insrt(self,v):
        if self.v:
            if v < self.v:
                if self.left == None:
                    self.left = Node(v)
                else:
                    self.left.insrt(v)
            elif v > self.v:
                if self.right == None:
                    self.right = Node(v)
                else:
                    self.right.insrt(v)
        else:
            self.v = v
         
    #print tree
    def display(self):
        if self.left:
            self.left.display()
        print(self.v,end=" ")
        if self.right:
            self.right.display()
            
root = Node(27)
root.insrt(14)
root.insrt(35)
root.insrt(10)
root.insrt(19)
root.insrt(31)
root.insrt(42)
root.display()
#-------------------------------------------------------
#constructing a BST from given list

#class to create node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
     
#constructing BST
def construct_tree(root, value):
    if root.value:
        if value < root.value:
            if root.left == None:
                root.left = Node(value)
            else:
                construct_tree(root.left, value)
        elif value > root.value:
            if root.right == None:
                root.right = Node(value)
            else:
                construct_tree(root.right, value)
    else:
        root.value = value
        
 #printing BST       
 def display(root):
    if root:
        display(root.left)
        print(root.value, end = " ")
        display(root.right)
         
            
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
root = Node()

for value in lst:
    construct_tree(root, value)
    
display(root)
