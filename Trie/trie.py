#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

#Trie:
#The root node of the trie always represents the null node.
#Each child of nodes is sorted alphabetically.
#Each node can have a maximum of 26 children (A to Z).
#Each node (except the root) can store one letter of the alphabet.

#Node Structure:
#Here we are using 3 items in a node :
#1.data -> stores the data that is character.
#2.child array -> it is an array that stores the address(to the next character node)
#respective to the character position(a = 0, b = 1, c = 3, d = 4....z = 25),and rest of the positions have None value.
#3.word end -> it is a variable that has a value 0 by default, whenever a word ends at the node then the node has word end value 1.
#The root node always has the data value None or *. Here we are using *.


class trieNode:
    def __init__(self, data):
        self.data = data
        self.child = [None]*26
        self.word_end = 0
        self.cp = 0
         
class trie:
    trie_root = None

    def __init__(self):
        self.trie_root = trieNode("*")
        
    #insert a word
    def insert(self, word):
        cur_node = self.trie_root  
        
        for indx in range(len(word)):
            pos = abs(ord("a") - ord(word[indx])) #finding postion for current character
            
            if cur_node.child[pos] == None:
                cur_node.child[pos] = trieNode(word[indx])  
            cur_node = cur_node.child[pos]
            
        cur_node.word_end = 1 #at the end of the word last character node will have word end = 1
        print("inserted")
        
    #to delete a word from trie we do not actually delete all the nodes of curresponding chracters.
    #intead we update the word end value of the last chracter og=f the word to 0.
    #that simply means no word ends at that character that indicates that word does not exists in the tire.
    #we do this to avoid losing other words having the same word as a prefix.
        
    #deleting a word
    def delete(self, word):
      cur_node = self.trie_root
         
      for indx in range(len(word)):
          pos = abs(ord("a") - ord(word[indx]))
            
          if cur_node.child[pos] is not None:
              cur_node = cur_node.child[pos]
          else:
              print("word does not exist")
              return
              
      if cur_node.word_end == 0:
          print("word does not exist")
          return 
          
      cur_node.word_end = 0
      print("deleted")
        
    #searching a word
    def search(self, word):
        cur_node = self.trie_root
         
        for indx in range(len(word)):
            pos = abs(ord("a") - ord(word[indx]))
            
            if cur_node.child[pos] == None:
                print("not found")
                return False
            cur_node = cur_node.child[pos]
            
        if cur_node.word_end == 1:
            print("found")
            return True
          
        print("not found")
        return False
      
trie = trie()
trie.insert("abcd")   #-->inserted
trie.insert("abcde")  #-->inserted
trie.insert("aefg")   #-->inserted
trie.search("aefg")   #-->found
trie.delete("aefg")   #-->deleted
trie.search("aefg")   #-->not found
trie.delete("mjdks")  #-->word does not exist.
      

        
        
        
        
