def count_chunks(grid):
    if not grid or not grid[0]:
        return "NULL"

    m, n = len(grid), len(grid[0])

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
            return
        # Mark the cell as visited
        grid[x][y] = '0'
        # Explore all four possible directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    chunk_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                # Found an unvisited chunk
                chunk_count += 1
                # Use DFS to mark all connected parts of the chunk
                dfs(i, j)

    return chunk_count if chunk_count > 0 else "NULL"

# Input reading


def main():
    import sys
    input = sys.stdin.read
    lines = input().split('\n')

    # First line contains dimensions
    m, n = map(int, lines[0].split())

    # The rest lines contain the grid
    grid = [list(line) for line in lines[1:m+1]]

    result = count_chunks(grid)
    print(result)


if __name__ == "__main__":
    main()
