#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#creating a complete binary tree by a given list.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
               
def construct_tree(lst, i, n):
    root = None
           
    if i < n:
        root = Node(lst[i])
               
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
               
    return root
  
  
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
