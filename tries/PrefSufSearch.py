"""
leetcode 745 thanks to u/otoc
time complexity is O(NM) where N is the number of words and M is the size of each word
space is O(alphabet_zie * key_length * N) where N is the number of keys in trie
"""


class TrieNode():
    def __init__(self):
        self.children = {}
        self.weight = -1

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    #trick is to insert every word with their pref/suf combo using a # for divider. so we can just search 
    #'pref#suf' in the trie
    # For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test"
    def insert(self, word, i):
	    # node.weight can be overwritten when a larger one is inserted
        node = self.root
        node.weight = i
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.weight = i
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weight
        
class WordFilter:
    def __init__(self, words: [str]):
        self.trie = Trie()
        i, n = 0, len(words)
        while i < n:
            l = len(words[i])
            for j in range(l + 1):
                self.trie.insert(words[i][j:l] + '#' + words[i], i)
            i += 1

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix + '#' + prefix)


