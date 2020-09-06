import unittest

def countArithmeticMean(arr:[int]):
    if not arr: return 0

    count = 0
    for i, v in enumerate(arr):
        left = findLeft(arr, i)
        right = findRight(arr, i)

        if 2 * v == left+right:
            count += 1
    print("arithmetic count is -> ",count)
    return count


def findLeft(arr:[int], index):
    if index-1 < 0:
        return 0
    else: return arr[index]

def findRight(arr:[int], index):
    if index+1 > len(arr)-1:
        return 0
    else: return arr[index]





















class MyTest(unittest.TestCase):
    def test_countArithmeticMean(self):
        self.assertEqual(countArithmeticMean([2,4,6,6,3]), 3)

if __name__ == '__main__':
    unittest.main()