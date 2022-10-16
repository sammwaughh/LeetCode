# Contains Duplicate

def containsDuplicate(nums):
    uniqs = []
    for x in nums:
        if x in uniqs:
            return True
        else:
            uniqs.append(x)
    return False

#print(containsDuplicate([1,2,3,1]))

# Above works but is too slow

def containsDuplicate2(nums):
    i = 0
    L = len(nums)
    while i < L-1:
        j = i + 1
        while j < L:
            if nums[i] == nums[j]:
                return True
            j += 1
        i += 1
    return False

print(containsDuplicate2([]))

## This is quadratic
## Need to sort in nlogn time then check in linear time