class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store each row, column and 3x3 grid in a list -> 27 entries
        # have each as separate lists for easier indexing
        # each index stores another list of elements within that row/col/3x3

        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]

        # use col to determine which entry of col to append to
        # use row to determine which entry of row to append to
        # use 3 // row and 3 // col to determine which 3x3 grid then conditionals
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                    
                grid = (row // 3) * 3 + (col // 3)

                if cur in cols[col] or cur in rows[row] or cur in grids[grid]:
                    return False

                cols[col].append(cur)
                rows[row].append(cur)
                grids[grid].append(cur)
        
        return True
