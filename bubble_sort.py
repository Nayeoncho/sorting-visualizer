# Implement bubble sort
def bubble_sort(array, stats):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            # Count each comparison
            stats["comparisons"] += 1
            if array[j] > array[j + 1]:
                # Swap adjacent element
                array[j], array[j + 1] = array[j + 1], array[j]
                # Count each swap
                stats["swaps"] += 1
            yield j, j+1
