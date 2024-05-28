"""
Implement a function that prints all paths that exist between two nodes (source to destination).
"""
import copy

from c_graph_algorithm.graph import Graph


def find_all_paths_recursive(graph, source, destination, path, paths, visited):
    visited[source] = True
    path.append(source)

    # Base Case
    if source == destination:
        paths.append(copy.deepcopy(path))
    # Recursive
    else:
        current = graph.graph[source]
        while current:
            vertex = current.vertex
            if not visited[vertex]:
                find_all_paths_recursive(graph, vertex, destination, path, paths, visited)

            current = current.next

    path.pop()
    visited[source] = False


def find_all_paths(graph, source, destination):
    """
    Finds all paths between source and destination in given graph
    :param graph: A directed graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    visited = [False] * graph.V

    path = []
    paths = []

    find_all_paths_recursive(graph, source, destination, path, paths, visited)

    return paths


# Main program to test above function
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(2, 5)

    print(find_all_paths(g, 0, 5))
