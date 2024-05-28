"""
You must implement the `remove_edge` function which takes a source and a destination as arguments.
If an edge exists between the two, it should be deleted.
Print the breadth-first traversal on the resultant graph.
"""
from collections import deque

from c_graph_algorithm.graph import Graph

"""
This challenge is very similar to the deletion in the linked list.
Our vertices are stored in a linked list. 
First, we access the source linked list. 
If the head node of the source linked list holds the key to be deleted, 
 we shift the head one step forward and return the graph.
If the key to be deleted is in the middle of the linked list, 
 we keep track of the previous node and connect the previous node with the next node when the destination encounters.
"""


def remove_edge(graph, source, destination):
    """
    A function to remove an edge
    :param graph: A graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    if graph.V == 0:
        return graph

    if source >= graph.V or source < 0:
        return graph

    if destination >= graph.V or destination < 0:
        return graph

    head = graph.graph[source]
    # If head node itself holds the key to be deleted
    if head and head.vertex == destination:
        graph.graph[source] = head.next
        return

    prev = None
    while head:
        if head.vertex == destination:
            break

        prev, head = head, head.next

    if head is None:
        return

    # Unlink the node from linked list
    prev.next = head.next


# Main program to test above function
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)

    print("Before: ")
    g.print_graph()

    remove_edge(g, 1, 3)

    print("After: ")
    g.print_graph()
