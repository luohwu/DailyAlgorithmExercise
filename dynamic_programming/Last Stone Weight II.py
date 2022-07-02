# https://leetcode.com/problems/last-stone-weight-ii/

from typing import List
class Solution:
    # split the stones into two parts
    # minimize the abs(difference between two parts)
    # dp[i][j]=True means the first (i-1) stones can  achieve weight j
    # Time: O(n*m), with n=len(stones), m=sum(stones)
    # Space: same
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_weight=sum(stones)
        n=len(stones)
        dp=[[False]*(sum_weight+1) for i in range(n+1)]

        #initialization
        for col in range(1,sum_weight+1):
            dp[0][col]=False
        for row in range(0,n+1):
            dp[row][0]=True

        # start dp
        for row in range(0,n):
            dp[row+1][row+1]=True
            for col in range(1,sum_weight+1):
                # print(row,col)
                if col>=stones[row]:
                    dp[row+1][col]=dp[row][col] or dp[row][col-stones[row]]
                else:
                    dp[row+1][col] = dp[row][col]

        # find the answer
        min_different=10**5
        for col in range(0,sum_weight):
            if dp[n][col] and abs(sum_weight-2*col)<min_different:
                # print(col)
                min_different=abs(sum_weight-2*col) # sum-a=b -> abs(b-a)=abs(sum-2a), thus minimize abs(sum-2a)
        return min_different


if __name__=='__main__':
    print(Solution().lastStoneWeightII(
        stones = [31,26,33,21,40]
    ))
