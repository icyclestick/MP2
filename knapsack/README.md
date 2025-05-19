"""
    Given the weight and value of each item and capacity of bag,
    find the combination of items to take such that the value of
    selected items in bag is maximum.
"""
"""
    Brute force solution:
        consider each combination of item(n) and select the one with maximum value
        Time complexity: O(2^n) -- exponential
        Space complexity: O(1)
        Since this method is exponential it will take lot, lot of time when there are more items
        the time to run algo will grow exponentially as number of items grows
    Naive Recursive solution:
        does the same thing as brute force, but instead of for loops we find solution
        by recursively calling function iteself
        Time complexity: O(2^n) -- exponential
        Space complexity: O(1)
        Note that the space complexity might be constant, but because we made recursive
        calls, there is space required for recursive call stack
    Memoization Recursive solution:
        does the same thing as naive recursive solution, but instead of calculating solution for
        each case, we track the previously calculated problem and its solutions
        Time complexity: O(n*c)
        Space complexity: O(n*c) + stack
        Note that because we made recursive calls here as well, it will also take space
        for call stack
    Dynamic Programming - Knapsack solution:
        same as recursive solution, but instead of making recursive calls each time, we store
        the output to array and get the value from array instead
        Time complexity: O(n*C)
        Space complexity: O(n*C)
"""