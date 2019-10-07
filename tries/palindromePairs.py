#leetcode 336

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.inputRef = None
        self.isEnd = False

class Solution:

    def __init__(self):
        self.root = self.getNewNode()

    def getNewNode(self):
        return TrieNode()

    def cnvrtChrToUni(self, char):
        return ord(char) - ord('a')

    def insert(self, word, inputRef):
        word = word[::-1]
        pCrawler = self.root
        length = len(word)

        for level in range(length):
            index = self.cnvrtChrToUni(word[level])

            if not pCrawler.children[index]:
                pCrawler.children[index] = self.getNewNode()
            pCrawler.inputRef = inputRef
            pCrawler = pCrawler.children[index]
        
        pCrawler.isEnd = True

    def search(self, word) -> int:
        pCrawler = self.root
        length = len(word)
        palString = ""
        ordMemo = None
        ref:int

        # palindroome matching needs more work
        for level in range(length):
            if pCrawler is None:
                break

            index = self.cnvrtChrToUni(word[level])
            ref = pCrawler.inputRef

            #gets the values that are palindrom
            if pCrawler.children[index]:
                palString += word[level]
                print(palString) 

            if not pCrawler.children[index]:
                return -1
             
            pCrawler = pCrawler.children[index]

        return ref

    def palindromePairs(self, words: [str]) -> [[int]]:

        pairs = []
        
        for word in words:
            self.insert(word, words.index(word))

        for word in words:
            returnVal = self.search(word)
            
            if returnVal != -1:
                pairs.append([words.index(word), returnVal])

        print(pairs)
            


s = Solution()
inputs = ["abcd","dcba","lls","s","sssll"]
s.palindromePairs(inputs)