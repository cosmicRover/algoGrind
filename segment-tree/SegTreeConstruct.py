# Segment tree is a DS that hleps with doing calcualtions in logarithmic times
# However it is somewhat difficult implement and needs to be tested throughly
# In this file fo example, sumRange has difficulties getting sum of range (0, 2)
# recommend using Binary Indexed Tree as it is more space efficient and easier to implement

class Solutions:
    def __init__(self, inputArr:[int]):
        self.arr = inputArr
        self.size = len(self.arr)
        self.tree = [0] * (self.size * 2) # init a tree of size 2 * len(original_input)

    def segTree(self):
        if len(self.arr) > 0:
            self.buildSegTree()

    #builds a segment tree from the given input
    def buildSegTree(self):
        #init i to size and j to 0
        i = self.size
        j = 0

        #while i < 2*original_arr_size and j is not len(original_input), increment both
        # this loop sets the original array elements as the leaf nodes
        while i < 2*self.size and j != self.size:
            self.tree[i] = self.arr[j]
            i += 1
            j += 1
        print(self.tree)

        # this loop bilds the sum from the leaf nodes, looping backwards
        i = self.size - 1
        while i > 0:
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1] # adding the elements
            i -= 1
            
        print(self.tree)

    # bug in this func. doesn't sum all the ranges properly
    def sumRange(self, left, right):

        # self.tree.pop(0)

        left += self.size
        right += self.size
        sum = 0

        while left <= right:
            if left % 2 == 1:
                print("left --->", left)
                sum += self.tree[int(left)]
                left += 1

            if right % 2 == 0:
                print("right --->", right)
                sum += self.tree[int(right)]
                right -= 1

            left /= 2
            right /= 2

        print(sum)


inputArr = [1, 2, 3, 4]
s= Solutions(inputArr)
s.segTree()
s.sumRange(0, 2)