best_x = None
best_cost = float("inf")

for x in range(2, 11):
    cost = 4 * x
    if cost < best_cost:
        best_cost = cost
        best_x = x

print("Best number of hours:", best_x)
print("Minimum cost:", best_cost)