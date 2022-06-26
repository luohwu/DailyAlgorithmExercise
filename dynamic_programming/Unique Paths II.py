# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    # similar to dynamic_programming/Unique Path
    # just mind the obstacle
    # Time: O(rows*cols)
    # Space: O(rows*cols)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        dp=[[1]*cols for i in range(rows)]

        #initialization for dp[0][0], dp[0][:], dp[:][0]
        dp[0][0]=1 if obstacleGrid[0][0]==0 else 0
        for col in range(1, cols):
            dp[0][col] = dp[0][col-1] if obstacleGrid[0][col] == 0 else 0
        for row in range(1, rows):
            dp[row][0] = dp[row-1][0] if obstacleGrid[row][0] == 0 else 0


        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col]==0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                else:
                    dp[row][col]=0
        return dp[-1][-1]