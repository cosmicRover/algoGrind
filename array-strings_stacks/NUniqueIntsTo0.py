'''
why does arr[i] = i*2 - n+1 work?
If you make a line on the x axis and start from -n and end at n,
you can plug the formula in to find n unique values that will
add up to 0. arr[0] = 0*2 - n+1 -> -4, arr[1] = -2 ... arr[4] = 4
'''

class Solution:
    # time and space O(n)
    def sumZero(self, n: int) -> [int]:
        arr = [0] * n
        i = 0
        while i < n:
            arr[i] = i*2 - n+1 # <- the formula
            i += 1
            
        return arr
        