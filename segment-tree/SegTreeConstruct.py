# Segment tree is a DS that hleps with doing calcualtions in logarithmic times
# import math

class SegmentTree:
    def __init__(self, values:[int]):
        self.tree = [0 for _ in values] + values
        self.treeSize = len(values)
        self.buildTree()

    #builds the segment tree
    def buildTree(self):
        #going through it reversed range 1 to treeSize
        for index in reversed(range(1, self.treeSize)):
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]

    #updates an element from the original input array
    def update(self, index, value):
        #prep the index to be on par with the tree sixe
        index += self.treeSize
        self.tree[index] = value
        
        #update the sum on tree
        while index > 1:
            index >>= 1 # right shift 1 is the same as right//2
            self.tree[index] = self.tree[2*index] + self.tree[2*index+1]

    #returns the precomputed sum of a given range
    def getSum(self, left, right) -> int:
        #bring the left and right sum upto par with the tree
        left += self.treeSize
        right += self.treeSize
        sum = 0

        # two pointer loop. if left mod has leftover 1, add to the sum and inc by 1
        while left <= right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            left >>= 1 # same as left = math.floor(left/2) 0r 5//2 -> 2

            #if right mod has no leftover, add to sum table and dec by 1
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            right >>= 1
        
        return sum


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    st = SegmentTree(arr)
    print(st.tree)
    print(st.getSum(0,2))
    st.update(2, 5)
    print(st.tree)
    print(st.getSum(0, 2))
