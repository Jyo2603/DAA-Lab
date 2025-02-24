def weighted_interval_scheduling(start, end, weight):
    jobs = sorted(zip(start, end, weight), key=lambda x: x[1])
    n = len(jobs)
    dp = [0] * (n + 1)
    
    for j in range(1, n + 1):
        include_weight = jobs[j-1][2]
        for i in range(j - 1, 0, -1):
            if jobs[i-1][1] <= jobs[j-1][0]:
                include_weight += dp[i]
                break
        dp[j] = max(include_weight, dp[j-1])
    
    return dp[-1]

start = list(map(int, input("Enter start times: ").split()))
end = list(map(int, input("Enter end times: ").split()))
weight = list(map(int, input("Enter weights: ").split()))

result = weighted_interval_scheduling(start, end, weight)

print("Maximum weight of non-overlapping intervals:", result)
