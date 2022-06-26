# https://leetcode.com/problems/triangle/

from typing import List
class Solution:
    # dp from top to bottom, row by row
    # Time O(n) beats 92.26%
    # Space O(n)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[10**5]*n for i in range(n)]
        dp[0][0]=triangle[0][0]
        # Only one possible path for the first column
        for row in range(1,n):
            dp[row][0]=dp[row-1][0]+triangle[row][0]

        # for each point [i,j],
        # there are two possible paths to reach it, namely [i-1,j] and [i-1,j-1]
        # just compare them
        for row in range(1,n):
            for col in range(1,row+1):
                dp[row][col]=triangle[row][col]+min(dp[row-1][col],dp[row-1][col-1])
        return min(dp[-1])


