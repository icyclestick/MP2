def MiddlemanJump(sortedArray, targetElement, k):
    leftSide = 0
    rightSide = len(sortedArray) - 1
    cur_pos = (leftSide + rightSide) // 2

    while True:
        prev_pos = cur_pos

        if sortedArray[cur_pos] == targetElement:
            return cur_pos # Target found at middle element or after a jump

        # If the target is on the left side of the array
        if targetElement < sortedArray[cur_pos]:
            cur_pos -= k
            if cur_pos < leftSide:
                cur_pos = leftSide
            if targetElement < sortedArray[leftSide]:
                return -1
            if targetElement > sortedArray[cur_pos]:
                    # Linear Search forward
                for i in range(cur_pos, prev_pos):
                    if sortedArray[i] == targetElement:
                        return i  # Target found
                return -1  # Target not in array

        # If the target is on the right side of the array
        elif targetElement > sortedArray[cur_pos]:
            cur_pos += k

            if cur_pos > rightSide:
                cur_pos = rightSide
                
            if targetElement > sortedArray[rightSide]:
                return -1

            if targetElement < sortedArray[cur_pos]:
                # Linear Search backward
                for i in range(cur_pos, prev_pos, -1):
                    if sortedArray[i] == targetElement:
                        return i  # Target found
                return -1  # Target not in array

    return -1  # Element not found


array_size = 20
k = 3
sortedArray = [1, 2, 4, 6, 8, 9, 12, 15, 19, 21, 22, 25, 26, 29, 31, 33, 45, 47, 49, 56]  
target = 56

result = MiddlemanJump(sortedArray, target, k)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found.")
