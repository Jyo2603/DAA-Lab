def subset_sum(nums, target):
    k = [False] * (target + 1)
    k[0] = True
    parent = [-1] * (target + 1)
    
    for i, num in enumerate(nums):
        for j in range(target, num - 1, -1):
            if k[j - num]:
                k[j] = True
                parent[j] = i

    if not k[target]:
        return False, []

    subset = []
    while target > 0:
        idx = parent[target]
        subset.append(nums[idx])
        target -= nums[idx]
    return True, subset

# Input handling
nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target sum: "))

exists, subset = subset_sum(nums, target)
if exists:
    print("Subset with the given sum exists:", subset)
else:
    print("Subset with the given sum does not exist")
