best_x = None
best_cost = float("inf")

# Iterate over all allowed values of x (hours)
# The server must run for at least 3 hours and not more than 9 hours
for x in range(3, 10):  # range(3, 10) covers x = 3, 4, ..., 9
    # Compute the total cost for each value
    cost = 5 * x

    # Check if this cost is lower than the current minimum
    if cost < best_cost:
        best_cost = cost
        best_x = x

# Print the optimal number of hours and the minimum cost
print("Optimal number of hours for backup system:", best_x)
print("Minimum total daily cost:", best_cost)