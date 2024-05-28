"""
The concept of loops or cycles is very common in graph theory.
A cycle exists when you traverse the graph and come upon a vertex which has already been visited.

You have to implement the detect_cycle function which tells you whether a graph contains a cycle.
"""
from c_graph_algorithm.graph import Graph


def detect_cycle(graph):
    visited = [False] * graph.V

    stack = [False] * graph.V

    for node in range(graph.V):
        if detect_cycle_recursive(graph, node, visited, stack):
            return True

    return False


def detect_cycle_recursive(graph, node, visited, stack):
    if stack[node]:
        return True

    if visited[node]:
        return False

    stack[node] = True
    visited[node] = True

    current = graph.graph[node]

    while current:
        if detect_cycle_recursive(graph, current.vertex, visited, stack):
            return True

        current = current.next

    stack[node] = False
    return False


# Main program to test the above code
if __name__ == "__main__":
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
