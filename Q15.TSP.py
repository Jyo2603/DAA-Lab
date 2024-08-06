def tsp_bruteforce(matrix):
    def visit(city, visited, current_length, path):
        if len(visited) == len(matrix):
            return current_length + matrix[city][0], path + [0]
        min_length = float('inf')
        best_path = None
        for next_city in range(len(matrix)):
            if next_city not in visited:
                next_length, result_path = visit(next_city, visited | {next_city}, current_length + matrix[city][next_city], path + [next_city])
                if next_length < min_length:
                    min_length = next_length
                    best_path = result_path
        return min_length, best_path

    n = len(matrix)
    length, path = visit(0, {0}, 0, [0])
    return path, length

# Input handling
n = int(input("Number of cities: "))
matrix = [list(map(int, input().split())) for _ in range(n)]
path, length = tsp_bruteforce(matrix)
print("Best path:", path)
print("Minimum length:", length)
