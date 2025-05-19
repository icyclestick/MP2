import itertools
from datetime import datetime

# example inputs
weights = [3, 8, 2, 5, 7, 9]
values =  [4, 12, 2, 7, 8, 10]
capacity = 20

# brute Force
max_val = 0
n = len(weights)
all_combinations = [[0, 1] for _ in range(n)]

print("Brute Force Tries:")
print("-------------------------------------------------------")
start_time = datetime.now()

for c in itertools.product(*all_combinations):# checks all the possible combonation
    val = 0
    w = 0
    for i in range(n):
        if w > capacity:
            break
        val += c[i] * values[i]
        w += c[i] * weights[i]

    print(f"Combination: {c} -> Weight: {w}, Value: {val}")
   
    if w <= capacity and val > max_val:
        max_val = val

end_time = datetime.now()
elapsed_time = (end_time - start_time).total_seconds()

#dipslay the result
print("-------------------------------------------------------")
print(f"\nBrute Force Result: {max_val}")
print(f"Execution Time: {elapsed_time:.6f} seconds\n")