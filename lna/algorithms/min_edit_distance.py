"""Solution for exercise 2.6/2.7
"""
# TODO: use ndarray of numpy replace original python list implementation(next PR)
from copy import deepcopy


def min_edit_distance(
        source: str,
        target: str,
        del_cost=1,
        ins_cost=1,
        sub_cost=2,
):
    """Minimum-Edit-Distance(DP)
    
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
    """Augmented minimum-edit-distance(DP) with alignment.
    
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
    # Use three tables for up, left and northwest or,
    # Uses one tables and represents up,
    # left and northwest as 1, 3, 5 respectivly?
    # 1: up, 3: left, 5: northwest, 4: up + left
    # 6: up + northwest, 8: left + northwest,
    # 9: up + left + northwest
    source_len = len(source)
    target_len = len(target)

    # Init matrix
    matrix = [[0 for _ in range(target_len + 1)]
              for _ in range(target_len + 1)]
    backtrace_table = deepcopy(matrix)
    backtrace_table[0][0] = -1
    for idx in range(1, source_len + 1):
        matrix[idx][0] = idx
        backtrace_table[idx][0] = 1
    for idx in range(1, target_len + 1):
        matrix[0][idx] = idx
        backtrace_table[0][idx] = 3

    traces_map = [1, 3, 5]
    min_cost = 0
    for i in range(1, source_len + 1):
        for j in range(1, target_len + 1):
            up = matrix[i - 1][j] + del_cost
            left = matrix[i][j - 1] + ins_cost
            northwest = matrix[i - 1][j - 1] \
                    + (sub_cost if source[i - 1] != target[j - 1] else 0)
            traces = [up, left, northwest]
            min_cost = min(traces)
            backtrace_table[i][j] = sum(traces_map[idx] for idx in range(3) \
                                  if traces[idx] == min_cost)
            matrix[i][j] = min_cost

    alignment = trace_back(backtrace_table, source, target)
    print('\n'.join(' '.join(triple[idx] for triple in alignment)
                    for idx in range(3)))

    return min_cost, alignment


def trace_back(backtrace_table, source, target):
    """Return an alignment from source to target.
    """
    # 1 for del, 3 for insert, 5 for nothing happened,
    # others for substitute.
    source_len = len(source)
    target_len = len(target)
    i, j = source_len, target_len
    # triple: operation, source[i], target[j]
    alignment = []

    while backtrace_table[i][j] != -1:  # i, j = 0, 0
        operation = backtrace_table[i][j]
        i -= 1
        j -= 1
        if operation == 1:
            alignment.insert(0, (source[i], '*', 'd'))
            j += 1
        elif operation in (3, 4):
            alignment.insert(0, ('*', target[j], 'i'))
            i += 1
        elif operation == 5:
            alignment.insert(0, (source[i], target[j], ' '))
        # Prefer substitution
        else:
            alignment.insert(0, (source[i], target[j], 's'))
    return alignment
