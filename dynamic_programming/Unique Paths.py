# https://leetcode.com/problems/unique-paths/

from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[-1][-1]

if __name__=='__main__':
    print(Solution().uniquePaths(m=3,n=7))