best_x = None
min_energy_consumption = float('inf')

# Iterate over all allowed integer values of x (number of active nodes)
# Constraints: 1 <= x <= 10
for x in range(1, 11):  # range(1, 11) covers x = 1, 2, ..., 10
    # Calculate the base computing energy
    e_base = x**2

    # Calculate the cooling overhead energy
    e_cool = 2**x

    # Calculate the total energy consumption
    current_energy_consumption = e_base + e_cool

    # Check if this energy consumption is lower than the current minimum
    if current_energy_consumption < min_energy_consumption:
        min_energy_consumption = current_energy_consumption
        best_x = x

# Print the optimal number of active nodes and the minimum total energy consumption
print(f"Optimal number of active nodes: {best_x}")
print(f"Minimum total energy consumption: {min_energy_consumption}")