def threeSumClosest(nums, target):
    # sort the array and then store the sum the first three index
    nums.sort()
    res = sum(nums[:3])

    # loop to iterate through each variable
    for i in range(len(nums)):

        # use two pointers to iterate through the array and compare to currentValue
        l, r = i+1, len(nums)-1
        
        # while left pointer is less than right
        while l < r:
            
            # s holds the currentValue that we will be comparing the target to
            s = sum((nums[i], nums[l], nums[r]))
            
            # we are comparing absolute value of sume - target and result - target
            # if its less, we assign sum to res
            if abs(s-target) < abs(res-target):
                res = s
            
            # advance the left/right pointers otherwise
            if s < target:
                l += 1 
            elif s > target:
                r -= 1
            else: # if none match, the size of array isn't long enough and return the original sum
                return res
    return res




array = [-1, 2, 1, -4]

result = threeSumClosest(array, 1)
print("closest value is ->>> %s" %result)

