# Fenwick or Binary Indexed Tree is a neat space/time efficient DS to calcualte range sum queries.
# This DS depends on finding the least significant bit. Find a lsb using num & -num expression

class FenwickTree:
    def __init__(self, inputArr:[int]):
        self.inputArr = inputArr
        self.buildPrefixTree()

    # Find a lsb using num & -num expression
    def calculateLSB(self, num):
        return num & -num

    def buildPrefixTree(self):
        self.inputArr = [0] + self.inputArr #add a 0
        
        for index in range(1, len(self.inputArr)): # loop through the range starting 1
            lsbIndex = index + self.calculateLSB(index) # find the least significant bit and add index to iy
            if lsbIndex < len(self.inputArr): # if index is < the total length, assigen it to array
                self.inputArr[lsbIndex] += self.inputArr[index]

    def _prefixQuery(self, index):
        #start from the top, make your way down
        index += 1
        result = 0
        while index:
            result += self.inputArr[index] # add to result
            index -= self.calculateLSB(index) # decrease LSB amount 
        return result

    # returns the query from end - (start -1) start -1 to balance the addition of 1
    def rangeQuery(self, startIndex, endIndex):
        return self._prefixQuery(endIndex) - self._prefixQuery(startIndex- 1)

    # add a value to a particular index on the finwick tree
    def addValueToTree(self, index, valueToAdd):
        index += 1
        while index < len(self.inputArr):
            self.inputArr[index] = self.inputArr[index] + valueToAdd
            index = index + self.calculateLSB(index)


arr = [1, 7, 3, 4]
ft = FenwickTree(arr)
print(ft.rangeQuery(0,0))
ft.addValueToTree(0, 2)
print(ft.rangeQuery(0,0))