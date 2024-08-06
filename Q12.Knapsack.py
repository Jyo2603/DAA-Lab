def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find the included items
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i)  # Store the 1-based index of the item
            w -= weights[i - 1]  # Reduce the capacity by the weight of the included item

    return dp[n][capacity], included_items

# Input handling
values = list(map(int, input("Enter the values of the items: ").split()))
weights = list(map(int, input("Enter the weights of the items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result, included_items = knapsack(values, weights, capacity)
print("The maximum value that can be obtained is:", result)
print("Items included (1-based index):", included_items)
