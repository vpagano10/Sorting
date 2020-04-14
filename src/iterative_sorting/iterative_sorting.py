a = [4, 8, 1, 6, 3, 9, 2, 5]


# TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element (hint, can do in 3 loc)
#         for x in range(i+1, len(arr)):
#             if arr[x] < arr[cur_index]:
#                 cur_index = x
#         # TO-DO: swap
#         if smallest_index != cur_index:
#             arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
#     return arr

# O(n^2)
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


print(selection_sort(a))


#
#
#
#
#


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         print(arr)
#         for x in range(len(arr) - 1):
#             if arr[x] > arr[x+1]:
#                 arr[x], arr[x+1] = arr[x+1], arr[x]
#     return arr

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# O(n^2)
def bubble_sort(arr):
    swap_occured = True
    while swap_occured:
        swap_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_occured = True
    return arr


print(bubble_sort(a))


#
#
#
#
#


# O(n)
# STRETCH: implement the Count Sort function below
# HINT: 3 for loops not nested
def count_sort(arr, maximum=-1):
    # do one loop to find max and min
    # do another loop to find how many of each

    return arr
