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

def mergeSort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    pivot = arr[0]
    a1 = []
    a2 = []
    for ele in arr[1:]:
        if ele < pivot:
            a1.append(ele)
        else:
            a2.append(ele)
    return mergeSort(a1) + [pivot] + mergeSort(a2)

def containsDuplicate3(nums):
    nums = mergeSort(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(set([1,3,1,4,4]))