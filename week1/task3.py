best_x = None
best_cost = float("inf")

# Iterate over all allowed values of x (hours)
# The application must be tested for at least 5 hours and no more than 12 hours
for x in range(5, 13):  # range(5, 13) covers x = 5, 6, ..., 12
    # Compute the total cost for each value
    cost = 3 * x

    # Check if this cost is lower than the current minimum
    if cost < best_cost:
        best_cost = cost
        best_x = x

# Print the optimal number of testing hours and the minimum cost
print("Optimal number of testing hours:", best_x)
print("Minimum total testing cost:", best_cost)