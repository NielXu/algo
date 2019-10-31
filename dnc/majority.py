"""
Suppose you’re consulting for a bank that’s concerned about fraud detection, and they come to you with the
following problem. They have a collection of n bank cards that they’ve confiscated, suspecting them of being used in
fraud. Each bank card is a small plastic object, containing a magnetic stripe with some encrypted data,
and it corresponds to a unique account in the bank. Each account can have many bank cards corresponding to it,
and we’ll say that two bank cards are equivalent if they correspond to the same account.

Their question is the following: among the collection of n cards, is
there a set of more than n/2 of them that are all equivalent to one another?
Assume that the only feasible operations you can do with the cards are
to pick two of them and plug them in to the equivalence tester. Show how
to decide the answer to their question with only O(n log n) invocations of
the equivalence tester.
"""
from typing import List, Optional, Tuple


def is_equivalent(a: str, b: str) -> bool:
    return a == b


def _half_equiv_helper(lst: List[str]) -> Optional[Tuple[str, int]]:
    """
    Return tuple of element that is the majority and the frequency of it, or None if it doesn't exist.
    """
    # trivially, 1 element array is always majority
    if len(lst) == 1:
        return lst[0], 1
    # otherwise, split in half.
    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]

    left_maj = _half_equiv_helper(left)
    right_maj = _half_equiv_helper(right)

    # both does not have majority, means no majority
    if left_maj is None and right_maj is None:
        return None

    # no left majority
    if left_maj is None:
        counter = right_maj[1]
        for left_element in left:
            if is_equivalent(left_element, right_maj[0]):
                counter += 1
        return (right_maj[0], counter) if counter > len(lst) / 2 else None

    # no right majority
    if right_maj is None:
        counter = left_maj[1]
        for right_element in right:
            if is_equivalent(right_element, left_maj[0]):
                counter += 1
        return (left_maj[0], counter) if counter > len(lst) / 2 else None

    # both has majority and is the same,
    if is_equivalent(left_maj[0], right_maj[0]):
        return left_maj[0], left_maj[1] + right_maj[1]

    # both has different majority
    counter = left_maj[1]
    for right_element in right:
        if is_equivalent(right_element, left_maj[0]):
            counter += 1
        if counter > len(lst) / 2:
            return left_maj[0], counter
    counter = right_maj[1]
    for left_element in left:
        if is_equivalent(left_element, right_maj[0]):
            counter += 1
    return (right_maj[0], counter) if counter > len(lst) / 2 else None


def half_equivalent(lst: List[str]) -> bool:
    """
    Return True if more than half of elements in `lst` is equivalent

    >>> half_equivalent(['a', 'a', 'a', 'c'])
    True
    >>> half_equivalent(['a', 'a', 'b', 'b'])
    False
    >>> half_equivalent(['a', 'b', 'c', 'd', 'e'])
    False
    >>> half_equivalent(['a', 'a', 'a', 'a', 'b', 'c', 'd'])
    True
    >>> half_equivalent(['a', 'a', 'a', 'b', 'c', 'd', 'e', 'f'])
    False
    >>> half_equivalent(['a', 'b', 'a', 'a', 'b', 'c'])
    False
    """
    return _half_equiv_helper(lst) is not None
