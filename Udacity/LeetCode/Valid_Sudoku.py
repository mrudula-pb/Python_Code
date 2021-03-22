# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution:
    def isValidSudoku(self, board):
        new_board = [[None] * len(board)] * len(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]  ".":
                    new_board[i][j] = board[i][j].replace(".", "0")
                else:
                    new_board[i][j] = board[i][j]
        for i in range(len(new_board)):
            for j in range(len(new_board)):
                if int(new_board[i][j]) != int(new_board[i][j]):
                    for i in range(len(new_board)):
                        for j in range(len(new_board)):
                            if new_board[i][j] != new_board[i][j]:
                                continue
                            else:
                                return False
                else:
                    return False
        return True

sol = Solution()
value = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]])

print(value)