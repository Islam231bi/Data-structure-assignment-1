# feel free to run this file and test the sorting algorithms
import random

from BubbleSort import BubbleSort
from HybridMergeSort import HybridMergeSort
from Merge import MergeSort
from QuickSort import QuickSort
from inersionSort import insertionSort
from selectionSort import SelectionSort

print("Using Selection sort: ", sep="\n")
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = SelectionSort(array)
sort.sort()
sort.displayResult()

print("Using Insertion sort: ", sep="\n")
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = insertionSort(array)
sort.sort()
sort.displayResult()

print("Using Bubble sort: ", sep="\n")
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = BubbleSort(array)
sort.sort()
sort.displayResult()

print("Using Merge sort: ", sep="\n")
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = MergeSort(array)
sort.m_sort()
sort.displayResult()

print("Using Hybrid merge sort: ", sep="\n")
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = HybridMergeSort(array, 4)

print("Using quick sort: ", sep="\n")
array = [3, 3, 2, 1, 1, 0, 10, -2, -2, -11, 1, 19, -9, 0, 0, 10, 100, 20]
sort = QuickSort()
sort.rando(array)
sort.quickSort(array, 0, len(array) - 1)
sort.displayResult(array)

print("Testing finding kth smallest element", sep="\n")
array = [3, 5, 6, 1, 2, 10]
sort = QuickSort()
new_array = sort.remove_duplicate(array)
sort.rando(new_array)
# k should be smaller than or equal to the number of distinct elements in the array
res = sort.kthSmallest(new_array, 0, len(new_array) - 1, 7)
print(res)
