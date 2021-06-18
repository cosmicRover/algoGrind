class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        sliding window approach. end in arr -> adjust start and maintain longest
        
        time O(n) | space O(1)
        '''
        start = 0
        longest = 0
        dic = {}

        for end in range(len(tree)):
            char = tree[end]

            #save frequency
            if char not in dic:
                dic[char] = 0

            dic[char] += 1

            #readjust start pointer while two fruits limit exceeds
            while len(dic) > 2:
                prev_char = tree[start]

                #decrrease fruit counter as start window moves more to the right
                dic[prev_char] -= 1
                if dic[prev_char] == 0:
                    del dic[prev_char]

                start += 1

            longest = max(longest, end-start+1)

        return longest
