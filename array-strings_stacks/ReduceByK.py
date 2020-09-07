'''
My attemp at the problem I was having tough time cracking.
Time O(n+groups) | Space O(group + recursive callstack) ?????
'''

def reduce(arr, k):
    group = helper(arr, k)
    
    s = ""
    for x in group:
        s += str(x)

    print(s)


def helper(sum, k):

    #group the sum
    count = 0
    group = []

    while count <len(sum):
        val = sum[count:count+k]
        count += k

        #get the total
        total = 0
        for x in val:
            total += int(x)

        group.append(total)

    # run recursively if needed more
    if len(group) > k:
        return helper(group, k)

    return group


s = "1111122222"
reduce(s, 2)