def weighted_interval_scheduling(starts, ends, weights):
    jobs = sorted(zip(starts, ends, weights), key=lambda x: x[1])
    n = len(jobs)
    dp = [0] * (n + 1)
    
    for j in range(1, n + 1):
        include_weight = jobs[j-1][2]
        for i in range(j - 1, 0, -1):
            if jobs[i-1][1] <= jobs[j-1][0]:
                include_weight += dp[i]
                break
        dp[j] = max(include_weight, dp[j-1])
    
    return dp[-1], jobs

starts = list(map(int, input("Enter start times: ").split()))
ends = list(map(int, input("Enter end times: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

result, jobs = weighted_interval_scheduling(starts, ends, weights)
print("start time\tend time\tweight")
for job in jobs:
    print(job[0], "\t\t", job[1], "\t\t", job[2])
print("Maximum weight of non-overlapping intervals:", result)