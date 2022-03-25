import random
import sys
from random import randrange


class QuickSort:
    def __init__(self):
        pass

    # this function removes duplicates from the array to be used in finding kth samlelst element
    def remove_duplicate(self, array):
        array = list(dict.fromkeys(array))
        return array

    # this function generates random pivot from the array
    def rando(self, array):
        x = random.randrange(0, len(array) - 1)
        (array[x], array[len(array) - 1]) = (array[len(array) - 1], array[x])

    # this function partitions the array according to the random pivot given from rando function
    def partition(self, array, left, right):
        pivot = array[right]
        i = left
        for j in range(left, right):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[right] = array[right], array[i]
        return i

    def quickSort(self, array, first, last):  # Quick sort function
        if first < last:
            pivot_index = self.partition(array, first, last)
            self.quickSort(array, first, pivot_index - 1)
            self.quickSort(array, pivot_index + 1, last)

    def displayResult(self, array):
        print("Sorted list: " + str(array), sep="\n")

    def kthSmallest(self, array, left, right, k):
        if k > right + 1 or k == 0:
            return "invalid index"
        if 0 < k <= right - left + 1:
            pos = self.partition(array, left, right)
            if pos - left == k - 1:
                return array[pos]
            if pos - left > k - 1:
                return self.kthSmallest(array, left, pos - 1, k)
            return self.kthSmallest(array, pos + 1, right, k - pos + left - 1)
        return sys.maxsize
