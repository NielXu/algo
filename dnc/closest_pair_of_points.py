"""
Algorithm to find the closest pair of points.

Running time of this D&C algorithm is O(nlogn)

http://www.cs.toronto.edu/~vassos/teaching/c73/handouts/closest-pair-of-points.pdf
"""
from typing import List, Tuple, Set
from math import sqrt


Coords = Tuple[int, int]


# helper methods
def distance(a: Coords, b: Coords) -> float:
    """
    Return the euclidean distance between `a` and `b`.

    Assume this is run in constant time.
    """
    return abs(sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))


def pairwise_closest_pair(a: Coords, b: Coords, c: Coords = None) -> Set[Coords]:
    """
    Calculates the pairwise distances and return the closest pair.

    Assume this is run in constant time.
    """
    # if there are only 2
    if c is None:
        return {a, b}

    # otherwise calculate pairwise distances
    d1, d2, d3 = (distance(a, b),
                  distance(a, c),
                  distance(b, c))

    min_dist = min(d1, d2, d3)
    if min_dist == d1:
        return {a, b}
    elif min_dist == d2:
        return {a, c}
    else:
        return {b, c}


def _rcp(sorted_x: List[Coords], sorted_y: List[Coords]) -> Set[Coords]:
    """
    Divide and conquer helper function.
    """
    # base case
    if len(sorted_x) <= 3:
        return pairwise_closest_pair(*sorted_x)
    else:
        # sorted_x divided by half
        lx = sorted_x[:len(sorted_x)//2]
        rx = sorted_x[len(sorted_x)//2:]

        # find the midpoint
        # m = (max x coordinate in lx + min x coordinate in rx) / 2
        m = (lx[-1][0] + rx[0][0]) / 2

        # sorted_y split based on lx and rx
        ly = [coord for coord in sorted_y if coord in lx]
        ry = [coord for coord in sorted_y if coord in rx]

        # recurse on left and right side.
        pl, ql = _rcp(lx, ly)
        pr, qr = _rcp(rx, ry)

        delta = min(distance(pl, ql), distance(pr, qr))

        # get sublist of sorted_y points whose x coordinates are within delta of m.
        b = [coord for coord in sorted_y if abs(coord[0] - m) < delta]

        if len(b) <= 1:
            if distance(pl, ql) <= distance(pr, qr):
                return {pl, ql}
            else:
                return {pr, qr}
        else:
            # placeholder for output
            p_opt, q_opt = b[0], b[1]

            # loop through all p in order
            for i, p in enumerate(b):
                # consider up to the next 7 points q after p on b
                for j in range(i + 1, min(len(b), i + 7)):
                    q = b[j]
                    if distance(p, q) < distance(p_opt, q_opt):
                        p_opt, q_opt = p, q
            if distance(p_opt, q_opt) < delta:
                return {p_opt, q_opt}
            elif distance(pl, ql) <= distance(pr, qr):
                return {pl, ql}
            else:
                return {pr, qr}


def closest_pair(p: List[Coords]) -> Set[Coords]:
    """
    Return the closest pair of coordinates by Euclidean distance.

    >>> a = closest_pair([(0, 1), (10, 2)])
    >>> a == {(0, 1), (10, 2)}
    True
    >>> a = closest_pair([(0, 0), (0, 1), (0, 10)])
    >>> a == {(0, 0), (0, 1)}
    True
    >>> a = closest_pair([(0, 0), (2, 1), (0, 10), (1, 100)])
    >>> a == {(0, 0), (2, 1)}
    True
    """
    # sorted by x
    sorted_x = sorted(p, key=lambda c: c[0])
    sorted_y = sorted(p, key=lambda c: c[1])

    return _rcp(sorted_x, sorted_y)
