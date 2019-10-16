#leetcode 684
#Time O(n^2) | space O(n*m)

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isEnd = False
        self.children = {}


class Trie:
    # https://leetcode.com/explore/learn/card/trie/147/basic-operations/1047/
    def __init__(self):
        self.root = TrieNode()

    #regular trie char insertion
    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEnd = True


    def find_prefix(self, word):
        node = self.root
        
        prefix = '' #keeps track of the visited chars
        
        for i in word:
            prefix += i
            
            if i not in node.children:
                return word
            else:
                #if a char is the end of a word, return prefix
                if node.children[i].isEnd:
                    return prefix
                else:
                    node = node.children[i]
        return word #if we have a match char by char, we return word


class Solution:
    def replaceWords(self, dict, sentence):
        tire = Trie()
        for i in dict:
            tire.insert(i)

        words=[]
        for i in sentence.split(sep=' '): #split the sentences into a list
            words.append(tire.find_prefix(i))
        return ' '.join(words) #join the list into a sentence when returning



dic =["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

s = Solution()
print(s.replaceWords(dic, sentence))
