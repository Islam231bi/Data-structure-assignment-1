import random
import time
import copy

from BubbleSort import BubbleSort
from GenerateArray import Generate
from Grapher import Grapher
from Merge import MergeSort
from QuickSort import QuickSort
from inersionSort import insertionSort
from selectionSort import SelectionSort
import sys

sys.setrecursionlimit(1500)

# Execution time samples for each algorithm
time_samples_merge = []
time_samples_quick = []
time_samples_insertion = []
time_samples_selection = []
time_samples_bubble = []

# Generating the array samples with different sizes


list_samples_x = [1000, 10000, 25000, 50000, 75000, 100000]
gen = Generate()
list_samples_quick = [gen.generate(1000), gen.generate(10000), gen.generate(25000), gen.generate(50000), gen.generate(75000), gen.generate(100000)]
# copying the same generated array to be used in the other sorting algorithms using deepcopy function in copy library
# we can not use normal (=) sign here as it will affect the original list
list_samples_merge = copy.deepcopy(list_samples_quick)
list_samples_insertion = copy.deepcopy(list_samples_quick)
list_samples_bubble = copy.deepcopy(list_samples_quick)
list_samples_selection = copy.deepcopy(list_samples_quick)

"""testing different sorting algorithms with the generated samples array"""

# testing quick sort
for array in list_samples_quick:
    sort = QuickSort()
    start = time.time()
    sort.rando(array)
    sort.quickSort(array, 0, len(array) - 1)
    end = time.time()
    time_samples_quick.append((end - start) * 1000)
    print("Running time for Quick sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + " sec\t",
          sep="\n")
print("\n")

# testing merge sort
for array in list_samples_merge:
    sort = MergeSort(array)
    start = time.time()
    sort.m_sort()
    end = time.time()
    time_samples_merge.append((end - start) * 1000)
    print("Running time for merge sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + " sec\t",
          sep="\n")
print("\n")

for array in list_samples_insertion:
    sort = insertionSort(array)
    start = time.time()
    sort.sort()
    end = time.time()
    time_samples_insertion.append((end - start) * 1000)
    print("Running time for insertion sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + " sec\t",
          sep="\n")
print("\n")

for array in list_samples_bubble:
    sort = BubbleSort(array)
    start = time.time()
    sort.sort()
    end = time.time()
    time_samples_bubble.append((end - start))
    print("Running time for bubble sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + " sec\t",
          sep="\n")
print("\n")

for array in list_samples_selection:
    sort = SelectionSort(array)
    start = time.time()
    sort.sort()
    end = time.time()
    time_samples_selection.append((end - start) * 1000)
    print("Running time for Selection sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + " sec\t",
          sep="\n")
print("\n")

# Graphing algorithms execution time with input
graph = Grapher()
graph.graph(list_samples_x, time_samples_merge, "Merge Sort")
graph.graph(list_samples_x, time_samples_quick, "Quick Sort")
graph.graph(list_samples_x, time_samples_selection, "Selection Sort")
graph.graph(list_samples_x, time_samples_bubble, "Bubble Sort")
graph.graph(list_samples_x, time_samples_insertion, "Insertion Sort")
graph.plotting()

