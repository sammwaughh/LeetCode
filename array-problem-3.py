# Rotate Array

def rotate1(nums, k):
    
    # [1, 2, 3, 4, 5, 6, 7], 2 -> [6, 7, 1, 2, 3, 4, 5]

    l = len(nums)
    firstBit = nums[l-k:l+1]
    secondBit = nums[:l-k]
    return firstBit + secondBit

rotate1([1,2,3,4,5,6,7], 2)

def rotate2(nums, k):
    # In place
    while k > 0:
        # Do one rotation to the right
        s = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            nums[i] = nums[i-1]
        k -= 1
        nums[0] = s
    return nums

#print(rotate2([1,2,3,4,5,6,7], 2))

def rotate3(nums, k):
    if k > 0:
        l = len(nums)
        k = k % l
        firstBit = nums[l-k:l+1]
        secondBit = nums[:l-k]
        nums2 = firstBit + secondBit
        for i in range(l):
            nums[i] = nums2[i]
    return nums


print(rotate3([1,2,3,4,5,6,7], 3))