def count_connected_hashes(grid, row, col, visited):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0
    
    if grid[row][col] == '.' or visited[row][col]:
        return 0
    
    visited[row][col] = True
    
    count = 1
    
    count += count_connected_hashes(grid, row + 1, col, visited)
    count += count_connected_hashes(grid, row - 1, col, visited)
    count += count_connected_hashes(grid, row, col + 1, visited)
    count += count_connected_hashes(grid, row, col - 1, visited)
    
    return count

def main():
    cols, rows = map(int, input("Enter input: ").split())
    grid = [list(input().split()) for _ in range(rows)]
    
    visited = [[False] * cols for _ in range(rows)]
    total_hashes = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '#' and not visited[row][col]:
                total_hashes += 1
                count_connected_hashes(grid, row, col, visited)
    
    print(total_hashes)

if __name__ == "__main__":
    main()
