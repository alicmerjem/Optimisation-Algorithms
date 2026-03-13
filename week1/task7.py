def maximize_profit(max_users, profit_basic, profit_premium):
    best_x = None
    best_y = None
    max_total_profit = -float('inf') # Initialize with negative infinity for maximization

    # Iterate over all possible values for x (Basic plan users)
    # x can range from 0 up to max_users
    for x in range(max_users + 1):
        # Iterate over all possible values for y (Premium plan users)
        # y can range from 0 up to max_users - x, to satisfy x + y <= max_users
        for y in range(max_users - x + 1):
            # Compute the total profit for the current combination (x, y)
            current_total_profit = (profit_basic * x) + (profit_premium * y)

            # Check if this total profit is higher than the current maximum
            if current_total_profit > max_total_profit:
                max_total_profit = current_total_profit
                best_x = x
                best_y = y

    return best_x, best_y, max_total_profit

# Given parameters for Task 7:
max_users_param = 20
profit_basic_param = 4
profit_premium_param = 7

# Call the function with the given parameters
optimal_x, optimal_y, max_profit = maximize_profit(
    max_users_param, profit_basic_param, profit_premium_param
)

# Print the results
print(f"Optimal Basic plan users (x): {optimal_x}")
print(f"Optimal Premium plan users (y): {optimal_y}")
print(f"Maximum total profit: {max_profit}")