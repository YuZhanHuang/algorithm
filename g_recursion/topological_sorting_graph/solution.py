from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


def helperFunction(my_graph, current_node, visited, result):
    visited[current_node] = True  # Mark the current node as visited

    # Recur for all the adjacent vertices of currentNode
    for i in my_graph.graph[current_node]:
        if visited[i] is False:
            helperFunction(my_graph, i, visited, result)
    result.insert(0, current_node)  # Push current vertex to result


def topologicalSort(my_graph):
    visited = [False] * my_graph.vertices  # Mark all the vertices as not visited
    result = []  # Our stack to store the result/output

    for current_node in range(my_graph.vertices):
        if visited[current_node] is False:
            helperFunction(my_graph, current_node, visited, result)

    return result


# Driver code
if __name__ == '__main__':
    # Create a graph given in the above diagram
    myGraph = Graph(5)
    myGraph.addEdge(0, 1)
    myGraph.addEdge(0, 3)
    myGraph.addEdge(1, 2)
    myGraph.addEdge(2, 3)
    myGraph.addEdge(2, 4)
    myGraph.addEdge(3, 4)

    print("Topological Sort")
    print(topologicalSort(myGraph))
