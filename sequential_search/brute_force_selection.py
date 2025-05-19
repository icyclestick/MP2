numbers = [12, 7, 19, 3, 15, 25, 8, 10, 42, 56, 77, 23, 89, 65, 33, 99, 14, 2, 37, 81,
           48, 64, 22, 91, 6, 40, 59, 87, 28, 53, 74, 9, 16, 39, 71, 93, 54, 32, 61, 27,
           35, 18, 49, 68, 83, 46, 57, 29, 95, 11, 26, 44, 78, 5, 66, 73, 41, 85, 31, 50,
           20, 63, 88, 34, 90, 60, 67, 4, 52, 36, 62, 80, 21, 84, 98, 13, 45, 69, 30, 38,
           47, 17, 92, 55, 70, 76, 82, 24, 43, 1, 100, 58, 96, 75, 97, 94, 86, 72, 51, 79]

def linear_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Run the function on the numbers list
target = 91
index = linear_search_iterative(numbers, target)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found!") 