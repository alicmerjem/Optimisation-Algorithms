def minimize_deployment_cost(min_a, max_a, min_b, max_b, cost_a, cost_b):
    best_x = None
    best_y = None
    min_total_cost = float('inf')

    # Iterate over all allowed values for Service A (x)
    for x in range(min_a, max_a + 1):
        # Iterate over all allowed values for Service B (y)
        for y in range(min_b, max_b + 1):
            # Compute the total cost for the current combination (x, y)
            current_total_cost = (cost_a * x) + (cost_b * y)

            # Check if this total cost is lower than the current minimum
            if current_total_cost < min_total_cost:
                min_total_cost = current_total_cost
                best_x = x
                best_y = y

    return best_x, best_y, min_total_cost

# Given parameters for Task 5:
min_a_param = 1
max_a_param = 6
min_b_param = 2
max_b_param = 8
cost_a_param = 5
cost_b_param = 3

# Call the function with the given parameters
optimal_x, optimal_y, min_cost = minimize_deployment_cost(
    min_a_param, max_a_param, min_b_param, max_b_param, cost_a_param, cost_b_param
)

# Print the results
print(f"Optimal instances for Service A (x): {optimal_x}")
print(f"Optimal instances for Service B (y): {optimal_y}")
print(f"Minimum total deployment cost: {min_cost}")