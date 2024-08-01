from itertools import permutations

def calculate_path_length(path, matrix):
    """Calculate the total length of a path."""
    return sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1)) + matrix[path[-1]][path[0]]

def tsp_bruteforce(matrix):
    """Solve the TSP using brute force."""
    n = len(matrix)
    cities = list(range(n))
    min_length = float('inf')
    best_path = None
    
    for perm in permutations(cities):
        length = calculate_path_length(perm, matrix)
        if length < min_length:
            min_length = length
            best_path = perm
            
    return best_path, min_length

def get_input_matrix():
    """Get distance matrix from user input."""
    n = int(input("Number of cities: "))
    print("Enter distance matrix:")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix

# Main execution
matrix = get_input_matrix()
path, length = tsp_bruteforce(matrix)
print("Best path:", path)
print("Minimum length:", length)
