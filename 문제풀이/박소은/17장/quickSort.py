# 퀵소트

def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        print(A)
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)

quicksort([2, 8, 7, 1, 3, 5, 6, 4], 0, 7)