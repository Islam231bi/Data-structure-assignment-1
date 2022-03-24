"""
Time complexity is O(N^2)
Space complexity is O(1)
Best case when array is sorted: O(N)
"""


class BubbleSort:

    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.passes = 0
        self.swaps = 0

    def sort(self):
        for i in range(self.size):
            flag = False
            self.passes += 1
            for j in range(self.size - i - 1):
                if self.array[j] > self.array[j + 1]:
                    flag = True
                    self.swaps += 1
                    (self.array[j], self.array[j + 1]) = (self.array[j + 1], self.array[j])
            if not flag:
                break

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")
