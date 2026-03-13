def minimize_storage_cost(min_gb, max_gb, cost_per_gb):
    best_x = None
    best_cost = float("inf")

    # Iterate over all allowed values of x (storage in GB)
    # The range should be inclusive of max_gb
    for x in range(min_gb, max_gb + 1):
        # Compute the total cost for each value
        cost = cost_per_gb * x

        # Check if this cost is lower than the current minimum
        if cost < best_cost:
            best_cost = cost
            best_x = x

    return best_x, best_cost

# Given parameters for Task 4:
min_gb_param = 20
max_gb_param = 100
cost_per_gb_param = 2

# Call the function with the given parameters
optimal_x, min_cost = minimize_storage_cost(min_gb_param, max_gb_param, cost_per_gb_param)

# Print the results
print("Optimal number: ", optimal_x)
print("Optimal storage: ", min_cost)