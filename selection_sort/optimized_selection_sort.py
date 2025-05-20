def min_max_selection(arr):
    n = len(arr) - 1

    i = 0
    j = n
    while i < j:
        min_index = i
        max_index = i
        swap_happened = False

        # Find the min and max in the current range
        for k in range(i, j + 1):
            if arr[k] < arr[min_index]:
                min_index = k
            if arr[k] > arr[max_index]:
                max_index = k

        # Swap minimum element to the front (index i)
        if arr[min_index] < arr[i]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap_happened = True

            # If we swapped with max_index, we need to update it
            if max_index == i:
                max_index = min_index

        # Swap maximum element to the end (index j)
        if arr[max_index] > arr[j]:
            arr[j], arr[max_index] = arr[max_index], arr[j]
            swap_happened = True

        # If no swaps happened, the array is already sorted
        if not swap_happened:
            break

        i += 1
        j -= 1


arr = [10, 21, 65, 9, 0, 2, 3, 77, 31, 9]
min_max_selection(arr)
print("Sorted array:", arr)
