class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # create sets
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subBoxSet = defaultdict(set)

        # go through entire board

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue

                # row check
                if board[row][col] in rowSet[row]:
                    return False
                else:
                    rowSet[row].add(board[row][col])
                
                # col check

                if board[row][col] in colSet[col]:
                    return False
                else:
                    colSet[col].add(board[row][col])
                
                # subBoxSet check
                # // 3 creates 3 groups

                if board[row][col] in subBoxSet[(row // 3, col // 3)]:
                    return False
                else:
                    subBoxSet[(row // 3, col // 3)].add(board[row][col])
        
        return True

        
        