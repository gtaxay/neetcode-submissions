class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rowLEN, colLEN = len(grid), len(grid[0])
        res = 0
        path = set()

        def dfs(row, col):
            # base zero or out of bounds
            if row < 0 or col < 0 or row >= rowLEN or col >= colLEN or grid[row][col] == "0" or (row, col) in path:
                return

            path.add((row, col)) 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rowLEN):
            for col in range(colLEN):
                if grid[row][col] == "1" and (row,col) not in path:
                    dfs(row,col)
                    res += 1
        
        return res

        