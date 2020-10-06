'''
The trick here is to understand the 3 differnt cases we need to work with plus
asking question/reading the prompts

Time O(n) | Space O(1)
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        * Each letter i, j has to be i < j order
        
        * Only check if two letters are not the same, check only once then break
        
        * According to dictionary order: smaller words come first
          i.e. app before apple
        '''
        
        #geiven order, hash it. format: c : index
        table = {k:v for v, k in enumerate(order)}
        
        #compare each word[i] to word[i+1] since we only care about right
        for i in range(len(words)-1): #-1 bc comare to one forward
            w1 = words[i]
            w2 = words[i+1]
            
            for x, y in zip(w1, w2): #gets same length chunk
                #compare if two chars not the same
                if x != y:
                    #get the orders
                    v1 = table[x]
                    v2 = table[y]
                    
                    if v1 > v2:
                        return False
                    
                    break #becuase we check only once when we encounter two diff characters
                    
            #outside of the loop when we break out of the loop or have same chars
            #we only check if the lengths are in correct order
            else: 
                if len(w1) > len(w2):
                    return False      
        return True