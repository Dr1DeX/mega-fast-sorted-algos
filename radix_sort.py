def radix_sort(arr):

    max_num = max(arr)
    exp_bit = 1

    def compa_counting(arr, exp_bit):
        n = len(arr)

        out = [0] * n

        count = [0] * 10

        for i in range(0, n):
            idx = arr[i] // exp_bit
            count[idx % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            idx = arr[i] // exp_bit
            out[count[idx % 10] - 1] = arr[i]
            count[idx % 10] -= 1
            i -= 1
        for i in range(0, len(arr)):
            arr[i] = out[i]

    while max_num / exp_bit >= 1:
        compa_counting(arr, exp_bit)
        exp_bit *= 10
