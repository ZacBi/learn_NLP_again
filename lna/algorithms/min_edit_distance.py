"""Solution for exercise 2.6/2.7
"""

# TODO: use ndarray of numpy replace original python list implementation


def min_edit_distance(
        source: str,
        target: str,
        del_cost=1,
        ins_cost=1,
        sub_cost=2,
):
    """minimum-edit-distance(DP)
    
    Args:
        `source`: source chars.
        `target`: target chars.
        `del_cost`: delete cost.
        `ins_cost`: insert cost.
        `sub_cost`: substitute cost.
        
    Returns:
        minimun edit distance between `source` and `target`

    Algorithm:
        D[i, j] = min(
                    D[i-1, j] + Del-cost(source[i]),
                    D[i, j-1] + Insert-cost(target[j]),
                    D[i-1, j-1] + Sub-cost(source[i] + target[j]),
                )
        D[i, j] is the cost from first i chars of source to,
        first j chars of target, and sub-cost is 0 while source[i]
        and target[j] is the same char, otherwise 2.
    """
    source_len = len(source)
    target_len = len(target)

    # Init matrix
    matrix = [[0 for _ in range(target_len + 1)]
              for _ in range(target_len + 1)]
    for idx in range(source_len + 1):
        matrix[idx][0] = idx
    for idx in range(target_len + 1):
        matrix[0][idx] = idx

    for i in range(1, source_len + 1):
        for j in range(1, target_len + 1):
            up = matrix[i - 1][j] + del_cost
            left = matrix[i][j - 1] + ins_cost
            northwest = matrix[i - 1][j - 1] \
                    + (sub_cost if source[i - 1] != target[j - 1] else 0)
            min_cost = min(up, left, northwest)
            matrix[i][j] = min_cost

    return matrix[source_len][target_len]


def min_edit_distance_pro(
        source: str,
        target: str,
        del_cost=1,
        ins_cost=1,
        sub_cost=2,
):
    """augmented minimum-edit-distance(DP)
    
    Args:
        `source`: source chars.
        `target`: target chars.
        `del_cost`: delete cost.
        `ins_cost`: insert cost.
        `sub_cost`: substitute cost.
        
    Returns:
        med: minimun edit distance between `source` and `target`
        matrix: 

    Algorithm:
        D[i, j] = min(
                    D[i-1, j] + Del-cost(source[i]),
                    D[i, j-1] + Insert-cost(target[j]),
                    D[i-1, j-1] + Sub-cost(source[i] + target[j]),
                )
        D[i, j] is the cost from first i chars of source to,
        first j chars of target, and sub-cost is 0 while source[i]
        and target[j] is the same char, otherwise 2.
    """
    pass