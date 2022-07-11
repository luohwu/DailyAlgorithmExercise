# https://leetcode.com/problems/pascals-triangle/

from typing import List

class Solution:

    # dp represents the Pascal's triangle.
    # Time: O(n^2)
    # Space: same
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        dp=[[0]*numRows for i in range(numRows)]
        for row in range(numRows):
            temp=[]
            for col in range(row+1):
                # elements on the edges
                if col==0 or col==row:
                    dp[row][col]=1
                # internal elements
                else:
                    dp[row][col]=dp[row-1][col-1]+dp[row-1][col]
                temp.append(dp[row][col])
            res.append(temp)
        return res



