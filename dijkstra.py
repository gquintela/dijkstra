from graph import *

from graph import *
from heapq import *

infinite = 99999

# v is contained in graph
def dijkstra(graph: Graph, v):
    output = []
    parent = {}
    vertices_seen = {}
    queue = []
    for vertex in graph.get_vertices():
        parent[vertex] = [None, infinite]
        vertices_seen[vertex] = False
        heappush(queue, (infinite, vertex, None))
    heappush(queue, (0, v, None))
    counter = len(vertices_seen)
    while counter != 0:
        u = heappop(queue)
        parent[u[1]] = [u[0], u[2]]
        if not vertices_seen[u[1]]:
            counter = counter - 1
            output.append(u[1])
            vertices_seen[u[1]] = True
            for neighbour in graph.get_neighbours(u[1]):
                if not vertices_seen[neighbour[0]]:
                    weight = graph.get_weight(u[1], neighbour[0])
                    heappush(queue, (weight, neighbour[0], u[1]))
    return parent


def get_dijkstra_path(graph: Graph, u, v):
    path = []
    path.insert(0, v)
    parents = dijkstra(graph, u)
    cost = 0
    parent = parents[v]
    while parent[1] != None:
        path.insert(0, parent[1])
        cost = cost + parent[0]
        parent = parents[parent[1]]
    print ("The path from " + str(u) + " to " + str(v) + " is: ", path)
    print("its cost is " + str(cost) + ".")
    return [path, cost]
