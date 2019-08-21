# Problem M1
# Solution

# O(N^2) time becasue of two loops| O(N) space because of trippletList


def threeSumSort(array: list, targetNum: int) -> [list]:
    array.sort()  # sort the arrayt first to prepare for in place comparison

    trippletList = []

    # -2 becasue we always want 3 numbers to be presnt when comparing
    for x in range(len(array)-2):

        # assigning the left and right pointers
        leftPointer = x + 1
        rightPointer = len(array) - 1

        # making sure the pointers dont overlap with the while loop
        while leftPointer < rightPointer:
            # assigning the currentNum to be compared and the currentSum to look
            currentNum = array[x]
            currentSum = currentNum + array[leftPointer] + array[rightPointer]

            # if they are eual, append to list and inc/dec the pointers
            if currentSum == targetNum:
                trippletList.append(
                    [currentNum, array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1

            # if less, increment left
            elif currentSum < targetNum:
                leftPointer += 1

            # if more, decrement right
            elif currentSum > targetNum:
                rightPointer -= 1

    # return the array at the end
    return trippletList


# test case
def test_threeSumSort():
    test_case = [12, 3, 1, 2, -6, 5, -8, 6]
    test_case_solution = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    target = 0

    assert threeSumSort(
        test_case, target) == test_case_solution, "should be [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]"


if __name__ == "__main__":
    test_threeSumSort()  # if test doesn't throw, print the next line
    print("test passed")
