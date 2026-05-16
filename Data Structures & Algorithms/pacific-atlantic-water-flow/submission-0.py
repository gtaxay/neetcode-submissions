class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
        rowLen, colLen = len(heights), len(heights[0])

        pacific, atlantic = set(), set()


        # add to sets
        def dfs(r, c, ocean, prevHeight):
            # stop case. Dont need to see if visited or out of bounds or higher
            if ((r,c) in ocean or r < 0 or c < 0 or r == rowLen or c == colLen or heights[r][c] < prevHeight):
                return

            ocean.add((r,c))
            dfs(r + 1, c,  ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])



            
            

            
        
        for c in range(colLen):
            # pacific
            dfs(0, c, pacific, heights[0][c])
            dfs(rowLen - 1, c, atlantic, heights[rowLen - 1][c])
        
        for r in range(rowLen):
            # pacific
            dfs(r, 0, pacific, heights[r][0])

            dfs(r, colLen - 1, atlantic, heights[r][colLen - 1])

        # go through every position and see if both in atlantic and pacific

        res = []
        for r in range(rowLen):
            for c in range(colLen):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])
        
        return res


        