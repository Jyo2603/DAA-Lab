def tsp_bruteforce(matrix):
    def visit(city, visited, current_length):
        if len(visited) == len(matrix):
            return current_length + matrix[city][0]
        min_length = float('inf')
        for next_city in range(len(matrix)):
            if next_city not in visited:
                next_length = current_length + matrix[city][next_city]
                min_length = min(min_length, visit(next_city, visited | {next_city}, next_length))
        return min_length

    n = len(matrix)
    return visit(0, {0}, 0)

# Input handling
n = int(input("Number of cities: "))
matrix = [list(map(int, input().split())) for _ in range(n)]
length = tsp_bruteforce(matrix)
print("Minimum length:", length)
