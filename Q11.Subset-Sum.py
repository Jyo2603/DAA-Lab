def find_subsets(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            results.append(path[:])
            return
        for i in range(start, len(nums)):
            if target >= nums[i]:
                path.append(nums[i])
                backtrack(i + 1, target - nums[i], path)
                path.pop()
    
    results = []
    backtrack(0, target, [])
    return results

# Input handling
nums = list(map(int, input().split()))
target = int(input())

subsets = find_subsets(nums, target)
if subsets:
    print("Subsets with the given sum:")
    for subset in subsets:
        print(subset)
else:
    print("No subset with the given sum exists")
