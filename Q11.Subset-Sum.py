def subset_sum(nums, target):
    k = [False] * (target + 1)
    k[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            k[j] = k[j] or k[j - num]
    
    return k[target]

nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target sum: "))

if subset_sum(nums, target):
    print("Subset with the given sum exists")
else:
    print("Subset with the given sum does not exist")
