
import selectionSort


class HybridMergeSort:
    def __init__(self, array, threshold):
        self.array = array
        # threshold value when reached, switch to selection sort
        self.threshold = threshold
        # calling sort function to sort the given array in constructor
        self.sort(self.array)
        # displaying the sorted array
        self.displayResult()

    def sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            # if the length of the array reached the threshold, switch to selection sort
            # I am using the already implemented selection sort algorithm
            if len(array) <= self.threshold:
                # creating new object to sort the left part of the array
                select_sort = selectionSort.SelectionSort(left)
                # sorting the left part of the array and updating the left array with the new sorted one
                left = select_sort.sort()
                # creating new object to sort the right part of the array
                select_sort2 = selectionSort.SelectionSort(right)
                # sorting the right part of the array and updating the right array with the new sorted one
                right = select_sort2.sort()
            # if the threshold is not reached, use merge sort
            else:
                self.sort(left)
                self.sort(right)
            # merging sorted left and right array , these array could be resulted from merge or selection sort according to thr threshold value
            self.merge(left, right, array)

    def merge(self, left, right, result):
        len_left = len(left)
        len_right = len(right)
        i = j = k = 0

        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
                k += 1
            else:
                result[k] = right[j]
                j += 1
                k += 1
        while i < len_left:
            result[k] = left[i]
            i += 1
            k += 1
        while j < len_right:
            result[k] = right[j]
            j += 1
            k += 1

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")

    def getArray(self):
        return self.array
