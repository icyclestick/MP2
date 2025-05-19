def optimized_bubble_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped and start < end:
        swapped = False
        last_swap_pos = 0

        # Pushes the largest element to the right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                last_swap_pos = i
        if not swapped:
            break
        
        # The new end is the last swap position
        end = last_swap_pos

        swapped = False
        last_swap_pos = 0

        # Pushes the smallest element to the left
        for i in range(end, start, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
                last_swap_pos = i
        
        # The new start is one past the last swap 
        start = last_swap_pos


arr = [9, 2, 3, 4, 10, 6, 7, 8, 1, 5]

print("Before sorting:", arr)
optimized_bubble_sort(arr)
print("After sorting: ", arr)