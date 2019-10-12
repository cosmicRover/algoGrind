class TrieNode:
    def __init__(self):
        #a dict that holds the children
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for w in word:
            #if letter already exists, go to the node
            if w in node.children:
                node = node.children[w]
            else:#init a new branch, and go to that node
                node.children[w] = TrieNode()
                node = node.children[w]
        #mark if it's an end of word
        node.isEnd = True

    def search(self, word):
        #use a stack to search
        # put root and word onto the stack to beign with
        stack = [(self.root, word)]
        
        while stack:
            node, w = stack.pop()

            if not w: #if no more word left
                if node.isEnd:
                    return True

            #check if word's prefix contains a "."
            #append the child node and word from the next index onward w[index:]
            elif w[0] == ".":
                for child in node.children.values():
                    stack.append((child, w[1:]))

            #check if w[0] is already in the children nodes
            else:
                if w[0] in node.children:
                    node = node.children[w[0]] #get the assocaite nodes to w[0]
                    stack.append((node, w[1:])) # append it
        return False #not found in the trie

words = ["mad", "dab", "bab"]
w = WordDictionary()
for word in words:
    w.addWord(word)
print(w.search("ad"))