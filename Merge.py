class MergeSort:

    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def m_sort(self):
        if self.size > 1:
            m = self.size//2
            l_arr = self.array[:m]
            r_arr = self.array[m:]

            leftsorter = MergeSort(l_arr)
            leftsorter.m_sort()
            rightsorter = MergeSort(r_arr)
            rightsorter.m_sort()
            i = 0
            j = 0
            k = 0

            while i < len(l_arr) and j < len(r_arr):
                if l_arr[i] < r_arr[j]:
                    self.array[k] = l_arr[i]
                    i += 1
                else:
                    self.array[k] = r_arr[j]
                    j += 1
                k += 1

            while i < len(l_arr):
                self.array[k] = l_arr[i]
                i += 1
                k += 1

            while j < len(r_arr):
                self.array[k] = r_arr[j]
                j += 1
                k += 1

    def displayResult(self):
        print("Sorted list: " + str(self.array), sep="\n")



