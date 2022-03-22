class QuickSort:
    def __init__(self, list1):
        self.list1 = list1

    def swap(self, num1, num2):  # for swapping
        temp = self.list1[num1]
        self.list1[num1] = self.list1[num2]
        self.list1[num2] = temp

    def partition(self, first, last, pivot):  # partition
        lasts1 = first
        self.swap(first, pivot)

        for unkown in range(first + 1, last + 1):
            if self.list1[unkown] < self.list1[first]:
                lasts1 += 1
                self.swap(unkown, lasts1)
        self.swap(first, lasts1)
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

