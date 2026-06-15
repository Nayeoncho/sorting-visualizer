def quick_sort(array, stats, low, high):
    # base code
    # If the range has 1 or 0 elements, stop recursion
    if low >= high:
        return

    # Partition the array and get the pivot's final position
    pivot_index = yield from partition(array, stats, low, high)

    # Recursively sort the left part (before pivot)
    yield from quick_sort(array, stats, low, pivot_index - 1)
    # Recursively sort the right part (after pivot)
    yield from quick_sort(array, stats, pivot_index + 1, high)

def partition(array, stats, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # i: Tracks the boundary of the smaller than pivot region
    i = low - 1

    # Walk through the array (except the pivot itself)
    for j in range(low, high):
        stats["comparisons"] += 1

        # Highlight current element being compared and the pivot
        yield j, high

        if array[j] <= pivot:
            # Expand the smaller region
            i += 1
            # Swap current element into the smaller region
            array[i], array[j] = array[j], array[i]
            stats["swaps"] += 1

            # Highlight the swapped position
            yield i, j

    # Move pivot to its correct final position
    array[i + 1], array[high] = array[high], array[i + 1]
    stats["swaps"] += 1

    # Highlight the pivot's final position
    yield i + 1, high

    # Return the pivot's final index
    return i + 1


