"""
Calculate the Number of Nodes in a Graph Level

Implement a function that returns the number of nodes at a given level starting from a root node of a directed graph.
Try modifying the breadth-first traversal algorithm to achieve this goal.

To solve this problem, all the previously-implemented data structures will be available to us.

Input
An **undirected graph** represented as an adjacency list, and the level whose number of nodes we need to find

Output
The number of nodes returned as a simple integer

"""
from collections import deque

from c_graph_algorithm.graph import Graph


def number_of_nodes(graph, level):
    """
    Calculates the number of nodes at given level
    :param graph: The graph
    :return: Total number of nodes at given level
    """
    source = 0
    visited = [0] * (len(graph.graph))

    queue = deque()
    queue.append(source)
    visited[source] = 1

    while queue:
        current = queue.popleft()
        node = graph.graph[current]

        while node:
            data = node.vertex
            if visited[data] == 0:
                queue.append(data)
                visited[data] = visited[current] + 1  # 標示vertex屬於第幾層
            node = node.next

    result = 0
    for i in range(len(graph.graph)):
        if visited[i] == level:  # 相加所有第i層的vertex
            result += 1

    return result


# Main to test above function
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print(number_of_nodes(g, 2))
