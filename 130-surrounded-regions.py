class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def markBorder(m, n):
            if (0 <= m < len(board) and 0 <= n < len(board[0])):
                if board[m][n] == "O":
                    board[m][n] = "Y"
                elif board[m][n] == "Y" or board[m][n] == "X":
                    return
                markBorder(m-1, n)
                markBorder(m+1, n)
                markBorder(m, n-1)
                markBorder(m, n+1)
        m = len(board)
        n = len(board[0])
        # Mark all border
        for i in range(m):
            markBorder(i, 0)
            markBorder(i, n-1)
        for j in range(n):
            markBorder(0, j)
            markBorder(m-1, j)
        # Now change Y back to O and O to X
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
