"""
Time complexity: O(N^2)
Space complexity: O(1)
Best case: O(N)
"""


class insertionSort:

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.sort()
        self.displayResult()

    def sort(self):
        for i in range(1, self.size):
            key = self.array[i]
            j = i-1
            while j >= 0 and self.array[j] > key:
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
