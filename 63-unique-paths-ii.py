class Solution:
    # BFS超时
    # def __init__(self) -> None:
    #     self.res = 0

    # def uniquePathsWithObstacles(self, obstacleGrid) -> int:
    #     def findPath(grid, x, y):
    #         if x < len(grid) and y < len(grid[0]):
    #             if grid[x][y] == 1:
    #                 return
    #             elif x == len(grid) - 1 and y == len(grid[0]) - 1:
    #                 self.res += 1
    #                 return
    #             findPath(grid, x+1, y)
    #             findPath(grid, x, y+1)
    #         else:
    #             return
    #     findPath(obstacleGrid, 0, 0)
    #     return self.res
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if (obstacleGrid == None or len(obstacleGrid) == 0):
            return 0
        else:
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            dp = [[0]*n for _ in range(m)]
            for i in range(m):
                if obstacleGrid[i][0] != 1:
                    dp[i][0] = 1
                else:
                  # Important because once there is an obstacle on the side, below can never be reached
                    break
            for j in range(n):
                if obstacleGrid[0][j] != 1:
                    dp[0][j] = 1
                else:
                    break
            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[m-1][n-1]


s = Solution()
obstacleGrid = [[0, 0], [1, 1], [0, 0]]
print(s.uniquePathsWithObstacles(obstacleGrid))
