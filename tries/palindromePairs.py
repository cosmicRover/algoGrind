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
            index = self.cnvrtChrToUni(word[level])
            ref = pCrawler.inputRef
            #gets the values that are palindrom
            if pCrawler.children[index]:
                palString += word[level]
                print(palString) 
            
            #if a char dont exist, what should happen to the rest of the chars ona word?
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

# here is one that doesn't use tries
# uses a dict and usually easier to understand 

# def palindromePairs(self, words):
#     d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
#     for i, w in enumerate(words):
#         for j in range(len(w)+1):
#             prefix, postfix = w[:j], w[j:]
#             if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
#                 res.append([i, d[prefix]])
#             if j > 0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
#                 res.append([d[postfix], i])
#     return res
