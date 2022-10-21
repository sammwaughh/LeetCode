# Move Zeroes

# Given an integer array nums, 
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(nums):
    i = 0
    j = 0
    l = len(nums)
    while j < l:
        val = nums[j]
        if val != 0:
            nums[i] = val
            i += 1
        j += 1
    while i < l:
        nums[i] = 0
        i += 1
    return nums

print(moveZeroes([0,1,0,3,12]))