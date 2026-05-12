class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 

        rowLen, colLen = len(grid), len(grid[0])
        path = set()

        def dfs(row, col):
            # stop case
            if row < 0 or col < 0 or row == rowLen or col == colLen or grid[row][col] == 0 or (row, col) in path:
                return 0
            
            path.add((row,col))

            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))


        for row in range(rowLen):
            for col in range(colLen):
                res = max(dfs(row, col), res)
        
        return res


        