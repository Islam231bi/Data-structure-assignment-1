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
array = [3, 1, 10, 5, 6, 7, 2, 11, 16]
sort = QuickSort(array)
sort.quickSort(0, len(array)-1, random.randrange(0, len(array)-1))
sort.displayResult()






