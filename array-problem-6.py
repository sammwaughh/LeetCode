# Intersection of Two Arrays II

# Return an array of the intersection of the two arrays

def intersect(nums1, nums2):
    intersection = []
    for ele in nums1:
        if ele in nums2:
            intersection.append(ele)
            nums2.remove(ele)
    return intersection

print(intersect([4,9,5], [9,4,9,8,4]))