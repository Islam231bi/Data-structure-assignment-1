"""
Time complexity is O(N^2)
Space complexity is O(1)
"""


class SelectionSort:

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def sort(self):
        for i in range(self.size - 1):
            min_idx = i
            for j in range(i + 1, self.size):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            if i != min_idx:
                (self.array[i], self.array[min_idx]) = (self.array[min_idx], self.array[i])
        # returning rested array for hybrid merge
        return self.array

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
