a = [4, 2, 6, 8, 5, 1, 3, 9, 7]
b = [5, 8, 1, 6, 7, 3, 9, 0, 2]


# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # set variable to traverse the merged_arr, arrA and arrB
    i = 0
    x = 0
    k = 0
    # while arrA has elements put them into the merged_arr
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    # when arrA is empty (all merged into the merged_arr), merge arrB's elements
    while x < len(arrB):
        merged_arr[k] = arrB[x]
        x += 1
        k += 1
    return merged_arr


print("merge, no sort of A and B", merge(a, b))

#
#
#
#
#


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        # split main arr
        mid = len(arr) // 2
        low_split = arr[:mid]
        high_split = arr[mid:]
        # recursively continue splitting
        merge_sort(low_split)
        merge_sort(high_split)
        # traverse splits
        i = 0
        x = 0
        # traverse main arr
        k = 0
        # merge sub-arrays back up into a sorted arr
        # check for the smallest element from the sub-arrays and push into main arr
        while i < len(low_split) and x < len(high_split):
            if low_split[i] < high_split[x]:
                arr[k] = low_split[i]
                i += 1
            else:
                arr[k] = high_split[x]
                x += 1
            k += 1
        # merge the remaining low_split elements into main arr if high_split is empty
        while i < len(low_split):
            arr[k] = low_split[i]
            i += 1
            k += 1
        # merge the remaining high_split elements into main arr if low_split is empty
        while x < len(high_split):
            arr[k] = high_split[x]
            x += 1
            k += 1
    return arr


c = merge_sort(a) + merge_sort(b)
print("merge_sort A", merge_sort(a))
print("merge_sort B", merge_sort(b))
print("list C", c)
print("List C in merge_sort", merge_sort(c))


#
#
#
#
#


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
