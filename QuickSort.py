import sys
from random import randrange


class QuickSort:
    def __init__(self, array):
        self.array = array

    def partition(self, first, last, pivot):  # partition
        lasts1 = first
        (self.array[first], self.array[pivot]) = (self.array[pivot], self.array[first])

        for i in range(first + 1, last + 1):
            if self.array[i] < self.array[first]:
                lasts1 += 1
                (self.array[i], self.array[lasts1]) = (self.array[lasts1], self.array[i])
        (self.array[first], self.array[lasts1]) = (self.array[lasts1], self.array[first])
        return lasts1

    def quickSort(self, first, last, pivot):  # Quick sort function
        if first < last:
            pivot_index = self.partition(first, last, pivot)
            self.quickSort(first, pivot_index - 1, first)
            self.quickSort(pivot_index + 1, last, last)

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")

    def kthSmallest(self, l, r, k, pivot):
        # If k is smaller than number of
        # elements in array
        if k > 0 and k <= (r - l + 1):
            # Partition the array around last
            # element and get position of pivot
            # element in sorted array
            pos = self.partition(l, r, pivot)

            # If position is same as k
            if pos - l == k - 1:
                return self.array[pos]
            if pos - l > k - 1:  # If position is more,
                # recur for left subarray
                return self.kthSmallest(self.array, l, pos - 1, k)

            # Else recur for right subarray
            return self.kthSmallest(self.array, pos + 1, r, k - pos + l - 1)

        return sys.maxsize
