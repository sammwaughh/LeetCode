# Intersection of Two Arrays II

# Return an array of the intersection of the two arrays

def intersect(nums1, nums2):
    intersection = []
    for ele in nums1:
        if ele in nums2:
            intersection.append(ele)
            nums2.remove(ele)
    return intersection

#print(intersect([4,9,5], [9,4,9,8,4]))

def intersect2(nums1, nums2):
    hashMap = {}
    for ele in nums1:
        if ele in hashMap.keys():
            hashMap[ele] += 1
        else: 
            hashMap[ele] = 1
    intersection = []
    for ele in nums2:
        if ele in hashMap.keys():
            if hashMap[ele] >= 1:
                intersection.append(ele)
                hashMap[ele] -= 1
    return intersection

print(intersect2([4,9,5], [9,4,9,8,4]))