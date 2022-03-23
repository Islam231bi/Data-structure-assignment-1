from matplotlib import pyplot as plt


class Grapher:
    def __init__(self):
        pass

    def graph(self, x, y, label):
        plt.plot(x, y, label=label)

    def plotting(self):
        plt.xlabel("Number of elements")
        plt.ylabel("Execution time (Milliseconds)")
        plt.title("sorting algorithms execution time")
        plt.legend()
        plt.show()
