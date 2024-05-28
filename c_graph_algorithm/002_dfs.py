"""
Implement Depth-First Graph Traversal

You have to implement the depth-first traversal in Python.

To solve this problem, the previously implemented graph class is already prepended.
"""
from c_graph_algorithm.graph import Graph


def dfs_helper(graph, source, visited):
    stack = [source]
    visited[source] = True
    result = ""

    while stack:
        current = stack.pop()
        result += str(current)

        node = graph.graph[current]

        while node:
            stack.append(node.vertex)
            visited[node.vertex] = True
            node = node.next

    return result, visited


def dfs(graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    visited = [False] * graph.V
    result, visited = dfs_helper(graph, 0, visited)

    for i in range(graph.V):
        if visited[i] is False:
            new_result, visited = dfs_helper(graph, i, visited)
            result += new_result

    return result


# Main to test the above program
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(dfs(g, 0))
