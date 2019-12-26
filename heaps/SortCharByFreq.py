#this is a lesson on using heapq to pack/unpack elements for consumptions
#O(n) yime and O(2n) extra space

import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        
        #store the frequencies O(n)
        dic = {}
        for x in s:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        
        #heappush to the heap array, this will sort the items from lowest to highest
        #heappush as a tuple of (frequency, [key]). It will be ordered by the frequencies O(n)
        heap = []
        for x in dic:
            key = x
            value = dic[x]
            heapq.heappush(heap, (value, [key]))
        
        #reuse dic to store the popped items
        dic = []
        
        #pop the items. It will pop from loweset to smallest, exact opposite direction of what we are looking for O(n)
        for _ in range(len(heap)):
            pair = heapq.heappop(heap)
            mul, key = pair[0], pair[1][0] #unpacking the elemnts 
            dic.append(key * mul) #multiply the key with the frequency when appending
            
        return ''.join(dic[::-1]) #return reversed
