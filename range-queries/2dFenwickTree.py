# Fenwick tree can be used to calculate range queries in multiple dimensions.
# 


class FenwickTree:
    def __init__(self, arr:[[int]]):
        self.arr = arr

        # self.ft = [[0 for _ in range(len(self.arr[0]))] for _ in range(len(self.arr))]
        # print(self.ft)

        for row in range(len(self.arr[0])):
            for column in range(len(self.arr)):
                self.update(row, column, self.arr[row][column])

    def getLSB(self, value):
        return value & (-value)

    def update(self, x, y, value):
        x_ = x
        while x_ < len(self.arr):
            x_ += self.getLSB(x_)
            y_ = y
            print("hello")
            while y_ < len(self.arr[0]):
                y_ += self.getLSB(y_)
                self.arr[x_][y_] += value
                print("hello 2")


inputArr = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
ft = FenwickTree(inputArr)
