# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n^2) solution

        n = 9  # n = m are square board of size 9

        for i in range(n):
            # rows
            digits_rows = set()
            digits_cols = set()
            for j in range(n):
                row_val, col_val = board[i][j], board[j][i]
                if row_val != ".":
                    if row_val in digits_rows:
                        return False
                    else:
                        digits_rows.add(row_val)
                if col_val != ".":
                    if col_val in digits_cols:
                        return False
                    else:
                        digits_cols.add(col_val)
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):

                grid_set = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i + k][j + l]
                        if val != ".":
                            if val in grid_set:
                                return False
                            else:
                                grid_set.add(val)

        return True