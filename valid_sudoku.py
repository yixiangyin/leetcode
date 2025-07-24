# ------------------------------------------------------------
# Problem: 36. Valid Sudoku
# URL: https://leetcode.com/problems/valid-sudoku/description/
# ------------------------------------------------------------
# Approach:
#   use a set to track whether you have seen the number before
#   1. do a sweep line by line horizontally
#   2. do a sweep line by line vertically
#   3. do a sweep square by square
#   isValidSudoku and isValidSudoku2 are similar 
#   isValidSudokuOnePass make only one pass
#   
#
# Complexity:
#   Time:  O(n^2)
#   Space: O(n^2)
# ------------------------------------------------------------
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # scan row by row
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur != ".":
                    if cur in s:
                        return False
                    else:
                        s.add(cur)
        # scan column by column
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                cur = board[j][i]
                if cur != ".":
                    if cur in s:
                        return False
                    else:
                        s.add(cur)
        # scan square by square
        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        cur = board[block_row+i][block_col+j]
                        if cur != ".":
                            if cur in s:
                                return False
                            else:
                                s.add(cur)
        return True                    

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
    def isValidSudokuOnePass(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
sol.isValidSudokuK(input)
