def sort_and_count(L):
    if len(L) <= 1:
        return 0, L
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]
    invL, sorted_left = sort_and_count(left)
    invR, sorted_right = sort_and_count(right)
    invS, sorted_list = merge_and_count(sorted_left, sorted_right)
    return invL + invR + invS, sorted_list

def merge_and_count(A, B):
    merged, inv, i, j = [], 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            inv += len(A) - i
            j += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    return inv, merged

def main():
    users = []
    for i in range(3):
        print("Enter song ranking for user", i+1, ":")
        user = list(map(int, input().split()))
        users.append(user)
    
    invB = sort_and_count(users[1])[0]
    invC = sort_and_count(users[2])[0]
    
    print("User 2 has", invB, "inversions.")
    print("User 3 has", invC, "inversions.")
    
    if invC < invB:
        print("User 3 has similar taste to user 1")
    elif invB < invC:
        print("User 2 has similar taste to user 1")
    else:
        print("All users have similar taste.")

if __name__ == "__main__":
    main()
