from dijkstra import *

# create dummy graph & driver test
my_graph = Graph()
my_graph.add_directed_edge('r', 's', 3)
my_graph.add_directed_edge('t', 'u', 3)
my_graph.add_directed_edge('w', 'x', 3)
my_graph.add_directed_edge('x', 'y', 3)
my_graph.add_directed_edge('r', 'v', 3)
my_graph.add_directed_edge('s', 'w', 3)
my_graph.add_directed_edge('t', 'x', 3)
my_graph.add_directed_edge('u', 'y', 3)
my_graph.add_directed_edge('t', 'w', 3)
my_graph.add_directed_edge('u', 'x', 3)


