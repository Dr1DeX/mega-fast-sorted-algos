def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[0: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2: len(arr)])
    l, r, k = 0, 0, 0
    res = [0] * len(arr)

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res[k] = left[l]
            l += 1
        else:
            res[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        res[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        res[k] = right[r]
        r += 1
        k += 1
    return res
