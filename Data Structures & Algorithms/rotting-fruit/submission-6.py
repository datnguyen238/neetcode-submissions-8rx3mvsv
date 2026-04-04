class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))

        if fresh == 0:
            return 0
        if not rotten:
            return -1
        
        minute = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        rotten.append((row,col))
            minute += 1

        if fresh == 0:
            return minute
        return -1

                