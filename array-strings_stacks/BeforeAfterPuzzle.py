'''
Time O(n) | Space O(2 * O(n) for first and last set)
'''


from collections import defaultdict

class Solution:
    def beforeAndAfterPuzzles(self, phrases: [str]) -> [str]:
        first = defaultdict(set)
        last = defaultdict(set)
        res = set()
        
        for p in phrases:
            words = p.split(' ')
            
            # match first or last word
            if words[0] in last:
                #| is inplace or. In set it unions two vars. |= -> union.add()
                # a gets the already added values from the set
                res |= {a + p[len(words[0]):] for a in last[words[0]]}
            
            if words[-1] in first:
                res |= {p + b for b in first[words[-1]]}
            
            '''
            inserting the phrases to first and last
            first loop will just trigger here
            first set adds everything after the first word, with first word as key
            second set adds the entire phrase p with last word as key
            '''
            first[words[0]].add(p[len(words[0]):])
            last[words[-1]].add(p)
        
        return sorted(list(res))