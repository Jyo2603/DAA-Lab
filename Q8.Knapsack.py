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
    return dp[n][capacity]

values = input("Enter the values of the items: ").split()
values = list(map(int, values))
weights = input("Enter the weights of the items: ").split()
weights = list(map(int, weights))
capacity = int(input("Enter the capacity of the knapsack: "))

result = knapsack(values, weights, capacity)
print("The maximum value that can be obtained is:", result)
