best_x = None
min_total_cost = float('inf')

# Iterate over all allowed integer values of x (number of features)
# Constraints: 1 <= x <= 10
for x in range(1, 11):  # range(1, 11) covers x = 1, 2, ..., 10
    # Calculate the technical debt cost
    technical_debt_cost = x**2

    # Calculate the feature value benefit
    feature_value_benefit = 6 * x

    # Calculate the total cost: technical debt cost - feature value benefit
    current_total_cost = technical_debt_cost - feature_value_benefit

    # Check if this cost is lower than the current minimum
    if current_total_cost < min_total_cost:
        min_total_cost = current_total_cost
        best_x = x

# Print the optimal number of features and the minimum total cost
print(f"Optimal number of features: {best_x}")
print(f"Minimum total development cost: {min_total_cost}")