class Solution:
    def findComplement(self, num: int) -> int:
        
        #converted to binary first, then find the complement, then return as int
        num = bin(num)[2:]
        newNum = "0b"
        
        for x in num:
            if x == "1":
                newNum += "0"
            else:
                newNum += "1"
                
        return int(newNum, 2)