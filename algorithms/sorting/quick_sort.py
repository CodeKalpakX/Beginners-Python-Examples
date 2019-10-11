# This is a simple implementation of the quicksort algorithm

# Call with the unsorted array, 0 and the length of the array

def quicksort(A, low, high):
    if low < high:
        m = partition(A, low, high)
        quicksort(A, low, m-1)
        quicksort(A, m+1, high)

def partition(A, low, high):
    pivot = A[low]
    i = low
    for j in range(low+1, high+1):
        if A[j] < pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    return i