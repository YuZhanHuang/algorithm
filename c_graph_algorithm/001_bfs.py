"""
Implement Breadth-First Graph Traversal

You have to implement the breadth-first traversal in Python.
To solve this problem, the previously implemented Graph class is already prepended.
"""
from collections import deque

from c_graph_algorithm.graph import Graph


def bfs_helper(graph, source, visited):
    queue = deque()
    queue.append(source)
    visited[source] = True
    result = ""

    while queue:
        current = queue.popleft()
        result += str(current)

        vertex = graph.graph[current]
        while vertex:
            queue.append(vertex.vertex)
            visited[vertex.vertex] = True
            vertex = vertex.next

    return result, visited


def bfs(graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    visited = [False] * graph.V
    result, visited = bfs_helper(graph, 0, visited)

    # graph is not 100% connected
    # travel left vertices if there exist.
    for i in range(graph.V):
        if visited[i] is False:
            new_result, visited = bfs_helper(graph, i, visited)
            result += result

    return result


# Main to test the above program
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(bfs(g, 0))
