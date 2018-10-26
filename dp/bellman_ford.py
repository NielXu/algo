"""
Problem:
We have a weighted graph with negative edge weights. Using a greedy algorithm
like Dijkstra's algorithm will not work for finding the shortest path from
a vertex to another vertex of a weighted graph, due to negative edge
weights.

Ideas:
This problem can be solved by the Bellman Ford algorithm.

Time Complexity:
O(|V||E|) where V are the number of vertices and E are the number of edges.

"""
def _get_source_weights(graph, dest):
    """ Return a list of (source, weight) pairs given a graph and the
    destination vertex """
    source_weights = []
    for source, dw_lst in graph.items():
        for destination, weight in dw_lst:
            if destination == dest:
                source_weights.append((source, weight))
    return source_weights


def bellman_ford(graph, target):
    """
    @param graph Dict[int, List[Tuple(int, float)]]: a dict-represented graph
    @param target int: the target vertex

    a graph is represented by a dictionary of the vertex id to a list of
    vertex, weight pairs. For example:
    
    @return Dict[int, float]: a dictionary representing the distance from
    all vertices to the target vertex.

    graph = {
        0: [(4, 3.), (1, 1.), (2, 1.)],
        1: [(4, 2.)],
        2: [(3, 1.)],
        3: [(4, 1.)],
        4: []
    }
    """
    # preset all distances to infinity, and successor node to None
    distances, successor, flagged = {}, {}, {}
    for v in graph:
        distances[v] = float('inf')
        successor[v] = None
        flagged[v] = False
    distances[target] = 0
    flagged[v] = True

    # loop from 0 to the number of vertices - 1
    # this will be the maximum number of iterations that this algorithm does
    for i in range(len(graph)):
        # if there is nothing flagged, break away
        if all(map(lambda x: not x, flagged)):
            break
        # loop through all the vertices
        for v in graph:
            # if v is updated in last iteration
            if flagged[v]:
                # loop through all the edges that links to v
                source_weights = _get_source_weights(graph, v)
                for source, weight in source_weights:
                    # replace it with the new distance if it is shorter
                    if distances[source] > distances[v] + weight:
                        distances[source] = distances[v] + weight
                        flagged[source] = 1
                        successor[source] = v
                flagged[v] = False
    return distances
