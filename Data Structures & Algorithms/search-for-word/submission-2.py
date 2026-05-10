class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # lengths
        ROWS, COLS = len(board), len(board[0])

        # current path so no repeats
        # use tuple to comare
        path = set()

        def backtrack(r, c, i):
            # made it to the end
            if i == len(word):
                return True
            # out of bounds, not equal, alr in path (cant use same one)
            if r < 0 or c < 0 or r >= ROWS or c >=COLS or word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))
            # back track
            res = (backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        
        # need to start backtrack at each node
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True

        return False
            

