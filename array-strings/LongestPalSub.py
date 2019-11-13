'''
Finding the longest palindromic substring using Manacher's Algo.
This algorithm is overkill on an interview and noone expects you to come up with this algo.
A more senseable solution would be with dp or expand around corners.
Time : O(n), worst case O(2n) when you end up expanding the right boundary towards the end of the string
Space : O(2*n + 2*n +2 ) for inserting '#' and mirror array
'''

#Manacher's algo
# class Solution:

#     def insertHashes(self, s:str) -> str:
#         # adding # inbetween the chars and $ and @ before and after
#         s = '#'.join('${}@'.format(s))
#         return s

#     def findMirrors(self, word:str):

#         #note we start from 1 and end at len -1 due to adding the special chars to signal start and end
#         mirrArr = [0] * len(word) #the arr to hold mirror distances
#         center = rBoundry = 0 #init pointers to 0

#         for index in range(1, len(word) -1): 
#             # formula to find a the mirror index of an element
#             mirr = 2*center - index

#             #save the min between boundry - index and mirror
#             if (index < rBoundry):
#                 mirrArr[index] = min(rBoundry-index, mirrArr[mirr])

#             #expand the rBoundry to find more of the palindrome.
#             while word[index + (1 + mirrArr[index])] == word[index - (1+ mirrArr[index])]:
#                 #inc value by 1 each time we find a matching pair
#                 mirrArr[index] += 1

#                 #readjust center rBoundry gets too big
#                 if (index + mirrArr[index] > rBoundry):
#                     center = index
#                     rBoundry = index + mirrArr[index]

#         print(mirrArr)
#         return mirrArr
   
#     def longestPalindrome(self, s: str) -> str:
#         newS = self.insertHashes(s)
#         arr = self.findMirrors(newS)

#         #find the max on the mirrArr and the center index
#         maxLen, centerIndex = max((n, i) for i, n in enumerate(arr))
#         print(centerIndex, maxLen)
        
#         #using the centerIndex and maxLen, find the start and end point
#         #by floor dividing them with 2 after sub/adding
#         start = (centerIndex - maxLen) //2
#         end = (centerIndex + maxLen) //2

#         #setup star, end with original input and return it
#         print(start, end)
#         pal = s[start:end]

#         return pal


#the expandaround corners algorithm. Just like manacher's algorithm, this algo exploits the fact that
# a plaindrome is a mirror image. It takes a point and expands around it until it hits un-mirrored elements



#expand around corners

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        
        for index in range(len(s)):
            #get two lens and get max of both
            len1 = self.expandOnCenter(s, index, index)
            len2 = self.expandOnCenter(s, index, index+1)
            maxLen = max(len1, len2)
            
            #rebalancing start/end with floor deivison
            if maxLen > (end - start):
                start = index - (maxLen -1) //2
                end = index + maxLen // 2
                
        return s[start:end+1]
            
    
    def expandOnCenter(self, s:str, left, right):

        print("coming in left ", left, "right ", right)
        
        # expand on the imaginary center with left and right
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        print("returning -> ",right, left)
        return right - left -1

s = Solution()
print(s.longestPalindrome("adal"))