import random


class QuickSort:
    def __init__(self, list1):
        self.list1 = list1

    def partition(self, first, last, pivot):  # partition
        lasts1 = first
        (first, pivot) = (pivot, first)

        for unkown in range(first + 1, last + 1):
            if self.list1[unkown] < self.list1[first]:
                lasts1 += 1
                (unkown, lasts1) = (lasts1, unkown)
        (first, lasts1) = (lasts1, first)
        return lasts1

    def quickSort(self, first, last, pivot):  # Quick sort function
        if first < last:
            pivotI = self.partition(first, last, pivot)
            self.quickSort(first, pivotI - 1, first)
            self.quickSort(pivotI + 1, last, last)

    def findKSamllest(self, K):  # The k function
        sum = 0
        for i in range(self.list1.__len__() - 1):
            if self.list1[i] == self.list1[i + 1]:
                if self.list1[i] <= self.list1[K + sum - 1]:
                    sum += 1
        return self.list1[K - 1 + sum]


a = [100, 50, 0, -10, 200, 98, 33]
o = QuickSort(a)

o.quickSort(0, len(o.list1) - 1, random.randrange(0, len(o.list1) - 1))
print(o.list1)

"""
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)"""
