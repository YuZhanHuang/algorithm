"""
Transpose a Graph
You have to implement a function which will take a graph as input and print its transpose.

               ┌────┐                              ┌────┐
               │  0 │                              │  0 │
               └─┬──┘                              └─▲──┘
                 │                                   │
          ┌──────┴───────┐                   ┌───────┴─────────┐
          │              │                   │                 │
       ┌──▼─┐         ┌──▼─┐              ┌──┴─┐            ┌──┴─┐
       │  1 │         │  2 │              │  1 │            │  2 │
       └─┬──┘         └────┘              └──▲─┘            └────┘
         │                                   │
    ┌────┴───────┐                           │
    │            │                    ┌──────┴──────┐
    │            │                    │             │
  ┌─▼──┐      ┌──▼─┐               ┌──┴─┐        ┌──┴─┐
  │  3 │      │  4 │               │  3 │        │  4 │
  └────┘      └────┘               └────┘        └────┘
"""
from c_graph_algorithm.graph import Graph


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


# Main program to test the above function
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    new_g = transpose(g)
    new_g.print_graph()
