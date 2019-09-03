from dijkstra import *

#example 1, directed graph
my_graph = Graph()
my_graph.add_directed_edge('a', 'b', 4)
my_graph.add_directed_edge('a', 'h', 8)
my_graph.add_directed_edge('b', 'c', 8)
my_graph.add_directed_edge('c', 'd', 7)
my_graph.add_directed_edge('b', 'h', 11)
my_graph.add_directed_edge('h', 'i', 7)
my_graph.add_directed_edge('i', 'c', 2)
my_graph.add_directed_edge('i', 'g', 6)
my_graph.add_directed_edge('h', 'g', 1)
my_graph.add_directed_edge('g', 'f', 2)
my_graph.add_directed_edge('c', 'f', 4)
my_graph.add_directed_edge('d', 'f', 14)
my_graph.add_directed_edge('d', 'e', 9)
my_graph.add_directed_edge('f', 'e', 10)

# get_dijkstra_path(my_graph, 'a', 'a')

#example 2, undirected graph
my_graph2 = Graph()
my_graph2.add_undirected_edge('s','t', 10)
my_graph2.add_undirected_edge('s','y', 5)
my_graph2.add_undirected_edge('t','x', 1)
my_graph2.add_undirected_edge('y','z', 2)
my_graph2.add_undirected_edge('t','y', 2)
my_graph2.add_undirected_edge('y','t', 3)
my_graph2.add_undirected_edge('x','z', 4)
my_graph2.add_undirected_edge('z','x', 6)
my_graph2.add_undirected_edge('y','x', 9)
my_graph2.add_undirected_edge('z','s', 7)

get_dijkstra_path(my_graph2, 't', 's')


