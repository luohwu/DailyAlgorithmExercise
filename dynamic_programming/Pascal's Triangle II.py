# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        dp=[[0]*(rowIndex+1) for i in range(rowIndex+1)]
        for row in range(rowIndex+1):
            for col in range(row+1):
                # elements on the edges
                if col==0 or col==row:
                    dp[row][col]=1
                # internal elements
                else:
                    dp[row][col]=dp[row-1][col-1]+dp[row-1][col]
                if row==rowIndex:
                    res.append(dp[row][col])
        return res