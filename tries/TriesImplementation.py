# An example of Trie implementation
# It takes into account the english alphabets as input

class TrieNode:
    def __init__(self):
        #init 26 children as none
        self.children = [None] * 26

        #a bool representing if it's an end of the word
        # it gets set to True if there are no more children on a particular branch
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        #returns new Trie node with 26 children init to None
        return TrieNode()

    #helper func that maps a provided char to an index
    #based on their unicode which can be found using ord()
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        # set prefixCrawl to thge root and get length of the input key
        prefixCrawl = self.root
        length = len(key)

        # a for loop through the length of key
        for level in range(length):

            # get the index of the char
            index = self._charToIndex(key[level])

            # if current node isn't present, init a new branch of TriNode()
            if not prefixCrawl.children[index]:
                prefixCrawl.children[index] = self.getNode()
            #set prefixCraw to the next node on the tree
            prefixCrawl = prefixCrawl.children[index]

        # mark the last node as the end
        prefixCrawl.isEndOfWord = True

    def search(self, key):
        # start from the root and loop through elemnts in key and search
        prefixCrawl = self.root
        length = len(key)
         
        for level in range(length):
            index = self._charToIndex(key[level])

            # if key doesn't exist in the tree, return False
            if not prefixCrawl.children[index]:
                return False
            #set prefixCraw to the next node on the tree
            prefixCrawl = prefixCrawl.children[index]

        return prefixCrawl != None and prefixCrawl.isEndOfWord



  
# Input keys (use only 'a' through 'z' and lower case) 
keys = ["the","a","there","anaswe","any", 
            "by","their"] 
output = ["Not present in trie", 
              "Present in trie"] 
  
# Trie object 
t = Trie() 
  
# Construct trie 
for key in keys: 
    t.insert(key) 
  
# Search for different keys 
print("{} ---- {}".format("the",output[t.search("the")])) 
print("{} ---- {}".format("these",output[t.search("these")])) 
print("{} ---- {}".format("their",output[t.search("their")])) 
print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  
