"""
Problem:
Shortest path

Find the shortest paths from a given vertex to all
other vertices in the graph G.

Ideas:
We can solve this problem by the Dijkstra's algorithm.

Running Time:
O(|V|*|E|) where V is vertices and E is edges

Addition:
The following implementation uses list and dict for
storing data. A better implementation would be using
heap to perform extract_min, and change_key. In that
way, the running time can be reduced to O((|V|+|E|)log|V|).
"""
import math


def get_edges(s, e):
    result = []
    for i in e:
        if i[0] == s:
            result.append(i)
    return result


def min_d(d, v, r):
    m = None
    for i in v:
        if i not in r:
            if not m:
                m = i
            else:
                m = m if d[m] < d[i] else i
    return m


def dijkstra_shortest_path(s, v, e):
    r = []
    d = {}
    for i in v:
        d[i] = math.inf
    d[s] = 0
    dep = 0
    while len(r) != len(v):
        node = min_d(d, v, r)
        r.append(node)
        for edge in get_edges(node, e):
            start, end, wt = edge
            if d[end] > d[node] + wt:
                d[end] = d[node] + wt
    return d


wt = dijkstra_shortest_path(
    'a',
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [
        ('a', 'b', 1),
        ('a', 'c', 6),
        ('a', 'd', 4),
        ('b', 'c', 2),
        ('b', 'e', 1),
        ('c', 'b', 1),
        ('c', 'd', 2),
        ('c', 'f', 2),
        ('d', 'c', 1),
        ('d', 'f', 1),
        ('e', 'f', 4),
        ('f', 'd', 3),
        ('f', 'e', 1)
    ]
)
print(wt)