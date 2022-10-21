# Single Number

def singleNumber(nums):
    seen = []
    for x in nums:
        if x not in seen:
            seen.append(x)
        else:
            seen.remove(x)
    return seen[0]

arr = [1,4,1,2,4]
print(singleNumber(arr))