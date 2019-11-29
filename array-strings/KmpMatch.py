'''
TODO: Only precompute part is implemented, needs the pattern matching part.
We use KMP to compute the longest prefix that is also the suffix. This comes in very handy
while checking for a pattern within a given string as it helps us not re-do work.
kmp can also be used for partial search, if that is relavent
'''

class Solution:
    def repeatedSubstringPattern(self, string: str, pattern: str):

        lspTable = self.kmpPrecompute(pattern)
        
        pPointer = sPointer = 0
        match = ""

        #match the pattern with original string
        while sPointer != len(string) and pPointer != len(pattern):
            
            #if a match, add to match and increment both pointers
            if string[sPointer] == pattern[pPointer]:
                match += pattern[pPointer]
                pPointer += 1
                sPointer += 1

            #if mismatch, reset match and send pPointer back to pPointer -1 from result
            #if the new pPointer and sPointer has a mismatch, inc sPointer by 1
            elif string[sPointer] != pattern[pPointer]:
                match = ""
                pPointer = lspTable[pPointer -1]
                if string[sPointer] != pattern[pPointer]: 
                    sPointer += 1

        #capable of partical match: s = "abcd" p = "abc", match = "abc"
        #must verify length to block a partical match
        print(match)
        # can alos find the index by subbing
        if len(match) == len(pattern):
            print(sPointer - pPointer)


    def kmpPrecompute(self, pattern):
        lspTable = [0] * len(pattern) #holds longest suf/[pref pattern]
        slow = 0
        fast = 1

        while fast < len(pattern):
            #if found a match, inc slow, copy slow for table[fast], inc fast
            if pattern[fast] == pattern[slow]: 
                slow += 1
                lspTable[fast] = slow
                fast += 1
            
            #if no match,
            else:
                #when slow isn't 0, slow takes it's previous value from lspTable
                if slow != 0:
                    slow = lspTable[slow-1]
                
                # if slow is 0, we insert 0 for lsp[fast] and increment fast
                else:
                    lspTable[fast] = 0
                    fast += 1
        return lspTable


s = Solution()
string = "abcdabdcabacab"
pattern = "caba"
s.repeatedSubstringPattern(string, pattern)