"""
Implement a function that tells us whether a graph is strongly connected or not.

A directed graph is strongly connected if there is a path between any two pairs of vertices.
"""
import copy

from c_graph_algorithm.graph import Graph


def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param visited:
    :param g: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result list
    result = []

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If an adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result


def transpose(graph):
    """
    Transpose the given graph
    :param graph: The graph
    :return: a new transposed graph of the given graph
    """
    new_graph = Graph(graph.V)
    graph.print_graph()

    for source in range(graph.V):
        node = graph.graph[source]

        while node:
            destination = node.vertex
            print('destination', destination, 'source', source)
            new_graph.add_edge(destination, source)
            node = node.next

    new_graph.print_graph()

    return new_graph


def is_strongly_connected(graph: Graph) -> bool:
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """
    # Step 1: Do DFS traversal starting from first vertex.
    visited = [False] * graph.V
    result = dfs(graph, 0, visited)

    # If DFS traversal does not visit all vertices, then return false
    if graph.V != len(result):
        return False

    # Step 2: Create a reversed graph
    graph2 = transpose(graph)

    # Step 5: Do DFS for reversed graph starting from first vertex.
    # Staring Vertex must be same starting point of first DFS
    visited = [False] * graph.V
    result = dfs(graph2, 0, visited)

    # If all vertices are not visited in second DFS, then
    # return false
    if graph2.V != len(result):
        return False

    return True


# Main program to test the above code
if __name__ == "__main__":
    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")

    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print("Yes" if is_strongly_connected(g2) else "No")
