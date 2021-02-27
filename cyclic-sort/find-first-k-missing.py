def find_first_k_missing_positive(nums, k):
    '''
    cycle sort approach. no range, range check and adjust new by -1

    time O(n + k, k is where we need to find remaining numbers) |
    space O(k, k is the number of items we want to return)
    '''
    n = len(nums)

    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    ans = []
    extranums = set() #use this to check numbers that already exist and out of place

    # find the missing numbers till k is 0
    for i, v in enumerate(nums):
        if i+1 != v:
            ans.append(i+1)
            extranums.add(v)
            k -= 1

        if k == 0:
            break

    # find the remaining missing numbers
    i = 1
    while k > 0:
        candidate = i + n
        if candidate not in extranums: #if the number don't exist, then append
            ans.append(candidate)
            k -= 1
        i += 1

    return ans


print(find_first_k_missing_positive([-2, -3, 4], 2))
