# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    # The idea is similar to dynamic_programming/Triangle.py
    # Time : O(rows*cols)
    # Space: O(rows*cols)
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[0]*cols for i in range(rows)]
        dp[0][0]=grid[0][0]
        for col in range(1,cols):
            dp[0][col]=dp[0][col-1]+grid[0][col]
        for row in range(1,rows):
            dp[row][0]=dp[row-1][0]+grid[row][0]
        for row in range(1,rows):
            for col in range(1,cols):
                dp[row][col]=grid[row][col]+min(dp[row-1][col],dp[row][col-1])
        return dp[-1][-1]


if __name__=='__main__':
    print(Solution().minPathSum(
        [[1, 2, 3], [4, 5, 6]]
    ))