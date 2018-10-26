"""
Problem:
(0-1) Knapsack problem.

A thief discovers a stash of various items
- The ith item has weight w_i and value v_i
- The thief can only carry W kilograms but wants to maximize the value.
- Either take one item or leave it.

Ideas:
We can define a recurrence relation with the following cases:

Case 1: Optimal solution selects item i
- New weight limit = w - w_i
- Optimal solution selects best of (1, 2,... i - 1) using new weight limit.

            | 0 if i = 0
opt(i, w) = | opt(i - 1, w) if w_i > w
            | max(opt(i - 1, w), v_i + opt(i - 1, w - w_i)) otherwise.

Time Complexity:
O(nW) where W is the weight

"""
def knapsack(items, weight) -> float:
    """  
    @param items List[Tuple(float, float)]: the items with (value, weight)
    @param weight int: weight that can be taken.
    
    @return float: the optimal value from items that can be taken based on
                   weight
                   
    Example:
    
    >>> items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
    >>> knapsack(items, 11)
    40
    """
    # use a memoization set. This will be a list of list, the outer list index
    # being the possible items considered, and the inner list being the
    # possible values given the maximum weight (from 0 to `weight`)
    opt = []
    for i in range(len(items)):
        opt.append([0] * (weight + 1))
    
    # loop through all the items and max weights starting from 1
    # when 0 possible items are considered, the value is trivally 0 for all
    # weights
    for i in range(0, len(items)):
        # consider the last item
        last_item = items[i]
        # weight + 1 because python range() is exclusive at the end
        for w in range(1, weight + 1):
            # if last item is leq total weight
            if last_item[1] <= w:
                # case 1: last item selected for optimal solution
                case1 = last_item[0] + opt[i - 1][w - last_item[1]]
                # case 2: last item not selected for optimal solution
                case2 = opt[i - 1][w]
                # select the max of case 1 and case 2
                opt[i][w] = max(case1, case2)

            # if last item is bigger than total weight
            # do not include last item
            else:
                opt[i][w] = opt[i - 1][w]
    
    # return the optimal value
    return opt[-1][-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
