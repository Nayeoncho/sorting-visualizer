# Implement merge sort
def merge_sort(array, stats, left, right):
    if right - left <= 1:
        return

    mid = (left + right) // 2

    # Sort half of the left part
    yield from merge_sort(array, stats, left, mid)

    # Sort half of the right part
    yield from merge_sort(array, stats, mid, right)

    # Merge step
    # [:] -> copying original array
    left_part = array[left:mid][:]
    right_part = array[mid:right][:]
    i = j = 0
    # 원본 배열에서 값을 채워넣을 위치
    k = left

    # Merge
    while i < len(left_part) and j < len(right_part):
        stats["comparisons"] += 1
        yield k, k
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        stats["swaps"] += 1
        k += 1

    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1