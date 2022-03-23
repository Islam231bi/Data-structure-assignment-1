from Grapher import Grapher

graph = Grapher()
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
y2 = [1,3,4,5]
y3 = [213,23,323,32]
y4 = [321,12,321,0]
y5 =[212,23,11,11]
graph.graph(x, y, "test")
graph.graph(x, y2, "test")
graph.graph(x, y3, "test")
graph.graph(x, y4, "test")
graph.graph(x, y5, "test")
graph.plotting()
