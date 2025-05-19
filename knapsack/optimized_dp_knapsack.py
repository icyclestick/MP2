from datetime import datetime

# example input
weights = [3, 8, 2, 5, 7, 9]
values = [4, 12, 2, 7, 8, 10]
capacity = 20

def dp_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]     # create a 2D list (DP table) with all values initialized to 0

    #fill the dp table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # max between including or excluding the current item
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]


    # backtracking to find items included in the optimal solution
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            included_items.append(i-1) # store the index of the included item
            w -= weights[i-1]


    included_items.reverse()
    return dp[n][capacity], included_items


#measure the execuiton time
start = datetime.now()
max_val, best_combination = dp_knapsack(weights, values, capacity)
end = datetime.now()
duration = (end - start).total_seconds()

# displays the most efficient combination
print("\n\nMost Efficient Combination (DP):")
print("-------------------------------------------------------")

for i in best_combination:
    print(f"  Item {i + 1}: Weight = {weights[i]}, Value = {values[i]}")

print("-------------------------------------------------------")
print(f"Maximum Value: {max_val}")
print(f"Execution Time: {duration} seconds")
print("\n")
