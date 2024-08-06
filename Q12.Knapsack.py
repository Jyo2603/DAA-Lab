def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find the included items
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], included_items

# Input handling
values = list(map(int, input("Enter the values of the items: ").split()))
weights = list(map(int, input("Enter the weights of the items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

result, included_items = knapsack(values, weights, capacity)
print("The maximum value that can be obtained is:", result)
print("Items included:", included_items)
