def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    # -1 → loop starts at the end of the array
    # 0 → loop stops before reaching 0 (so it ends at 1)
    # -1 → counts downward

    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize boolean swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark swapped as true when a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


arr = [6,6,2,5,7,9]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)