#leetcode 692
# don't use this, solution can be optimized further
# for example, with pq

from collections import Counter

class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        #counts the frequency of items, same as making a dict to a add freq
        counts = Counter(words)
        print(counts)

        items = list(counts.items())
        print(items)

        items.sort(key=lambda item: (item[1], item[0]))
        print(items)

        
s = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
s.topKFrequent(words, 2)