'''
using a prefix array to build the multiplication list.
'''
class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1] * num) #multiply arr's last number with new num and store it
            
    def getProduct(self, k: int) -> int:
        if k > len(self.arr) -1: return 0
        
        index = -k - 1
        return int(self.arr[-1] / self.arr[index]) #since we multiplied everything, if we divide by the proper index, we will find the value