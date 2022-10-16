# Remove Duplicates from Sorted Array
# Must sort in-place

arr = [1,1,2,3,4,4,4,7,7,8,10]

def removeDups(nums):
    uniqArr = []
    for x in nums:
        if x not in uniqArr:
            uniqArr.append(x)
    for i in range(len(uniqArr)):
        nums[i] = uniqArr[i]
    return len(uniqArr)
    
## Above works

def betterRemoveDups(nums):
    writeIndex = 1
    L = len(nums)
    k = 1
    for readIndex in range(1, L):
        if nums[readIndex] != nums[readIndex - 1]:
            nums[writeIndex] = nums[readIndex]
            writeIndex += 1
            k += 1
    return k

print(betterRemoveDups(arr))
