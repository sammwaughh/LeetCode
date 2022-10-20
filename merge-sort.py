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

arr = [10, 7, 1, 3, 4, 5, 9, 8, 2, 6]
print(mergeSort(arr))


    