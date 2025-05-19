import itertools
from datetime import datetime

def brute_force(weights, values, capacity):
    max_val = 0
    n = len(weights)
    all_combinations = [[0,1] for i in range(n)]

    for c in itertools.product(*all_combinations):
        val = 0
        w = 0
        for i in range(len(c)):
            if w > capacity:
                break

            val += c[i] * values[i]
            w += c[i] * weights[i]

        if w <= capacity and val > max_val:
            max_val = val

    return max_val


def naive_recursive_solution(weights, values, capacity):
    if not weights or capacity <= 0:
        return 0

    if weights[0] <= capacity:
        return max(
            values[0] + naive_recursive_solution(weights[1:], values[1:], capacity-weights[0]), 
            naive_recursive_solution(weights[1:], values[1:], capacity))
    else:
        return naive_recursive_solution(weights[1:], values[1:], capacity)


def memoization_recursive_solution(weights, values, capacity):
    data = [[-1]*(capacity+1) for _ in range(len(weights)+1)]

    def solve(weights, values, capacity):
        n = len(weights)
        if data[n][capacity] != -1:
            return data[n][capacity]

        if not weights or capacity <= 0:
            return 0

        if weights[0] <= capacity:
            data[n][capacity] = max(
                values[0] + solve(weights[1:], values[1:], capacity-weights[0]), 
                solve(weights[1:], values[1:], capacity))
        else:
            data[n][capacity] = solve(weights[1:], values[1:], capacity)
        return data[n][capacity]

    return solve(weights, values, capacity)


def knapsack_solution(weights, values, capacity):
    if not weights or capacity <= 0:
        return 0

    n = len(weights)
    data = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                data[i][j] = max(values[i-1] + data[i-1][j-weights[i-1]], data[i-1][j])
            else:
                data[i][j] = data[i-1][j]
    return data[-1][-1]


examples = [
    [[1, 2, 3], [10, 15, 40],  6],
    [[10, 20, 30], [60, 100, 120],  50],
    [[1, 2], [10, 15],  6],
    [[1, 2, 3, 4, 5], [10, 15, 10,20,30],  6],
    [[1, 2, 3, 4, 5,8,6,4,2,4,6,78,9,97,66,53,2],
     [10, 15, 10,20,30,34,2,34,23,53,74,32,39,86,50,36,20],  140],
]
l = [[1, 2, 3, 4, 5,8,6,4,2,4,6,78,9,97,66,53,2, 1, 2, 3, 4, 5,8,6,4,2,4,6,78,9,97,66,53,20],
     [10, 15, 10,20,30,34,2,34,23,53,74,32,39,86,50,36,20, 10, 15, 10,20,30,34,2,34,23,53,74,32,39,86,50,36,20],
     500]
a = 1032
results = [
    65, 220, 25, 40, 418
]

print("maximum total value:")
print(knapsack_solution(*examples[0]))

for i in range(len(examples)):
    time = datetime.now()
    assert brute_force(*examples[i]) == results[i]
    time1 = (datetime.now() - time).total_seconds()
    time = datetime.now()
    assert naive_recursive_solution(*examples[i]) == results[i]
    time2 = (datetime.now() - time).total_seconds()
    time = datetime.now()
    assert memoization_recursive_solution(*examples[i]) == results[i]
    time4 = (datetime.now() - time).total_seconds()
    time = datetime.now()
    assert knapsack_solution(*examples[i]) == results[i]
    time = datetime.now()
    time3 = (datetime.now() - time).total_seconds()
    print(f"""
        Items: {len(examples[i][0])} Brute force: {time1}, Naive Recursive: {time2}, 
        Memoization Recursive: {time4} Knapsack: {time3}""")