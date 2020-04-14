a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
b = [4, 5, 19, 1, 10, 3, 8, 16, 17, 9, 12, 7, 15, 11, 2, 13, 14, 18, 6]


# STRETCH: implement Linear Search
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


print(linear_search(b, 3))


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


print(binary_search(a, 10))


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid-1)
    else:
        return binary_search_recursive(arr, target, mid+1, high)


print(binary_search_recursive(a, 4, 0, len(a)))
