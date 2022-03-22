import random
import time
import matplotlib as plt

from GenerateArray import Generate
from Grapher import Grapher
from Merge import MergeSort
from QuickSort import QuickSort
from inersionSort import insertionSort
from selectionSort import SelectionSort

time_samples_merge = []
time_samples_quick = []
time_samples_insertion = []
time_samples_selection = []

"""Generating the array samples with different sizes"""
list_samples = []
list_samples_x = [1000, 10000, 25000, 50000, 75000, 100000]
gen = Generate()
list_1000 = gen.generate(1000)
list_samples.append(list_1000)
list_10000 = gen.generate(10000)
list_samples.append(list_10000)
list_25000 = gen.generate(25000)
list_samples.append(list_25000)
list_50000 = gen.generate(50000)
list_samples.append(list_50000)
list_75000 = gen.generate(75000)
list_samples.append(list_75000)
list_100000 = gen.generate(100000)
list_samples.append(list_100000)

"""testing different sorting algorithms with the generated samples array"""

# testing merge sort
for array in list_samples:
    sort = MergeSort(array)
    start = time.time()
    sort.m_sort()
    end = time.time()
    time_samples_merge.append((end - start) * 1000000)
    print("Running time for merge sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + "sec\t", sep="\n")

print("\n")

# testing quick sort
for array in list_samples:
    sort = QuickSort(array)
    start = time.time()
    sort.quickSort(0, len(array) - 1, random.randrange(0, len(array) - 1))
    end = time.time()
    time_samples_merge.append((end - start) * 1000000)
    print("Running time for Quick sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + "sec\t", sep="\n")

print("\n")

# for array in list_samples:
#     sort = SelectionSort(array)
#     start = time.time()
#     sort.sort()
#     end = time.time()
#     time_samples_selection.append((end - start) * 1000000)
#     print("Running time for Selection sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + "sec\t", sep="\n")
#
# print("\n")
#
# for array in list_samples:
#     sort = insertionSort(array)
#     start = time.time()
#     sort.sort()
#     end = time.time()
#     time_samples_insertion.append((end - start) * 1000000)
#     print("Running time for insertion sort with size\t" + str(len(array)) + " is:\t" + str(end - start) + "sec\t", sep="\n")
#
# print("\n")

graph = Grapher()
graph.graph(list_samples_x, time_samples_merge, "Merge Sort")
# graph.graph(list_samples_x, time_samples_selection, "Selection Sort")
# graph.graph(list_samples_x, time_samples_insertion, "Insertion Sort")
graph.graph(list_samples_x, time_samples_quick, "Quick Sort")
graph.plotting()
