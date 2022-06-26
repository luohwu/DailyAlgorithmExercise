# https://leetcode.com/problems/integer-break/

class Solution:
    # dp[i] means the answer of integerBreak(i)
    # dp[i]=max(dp[i],j*dp[i-j],j*(i-j))
    # it's important to add j*(i-j), because the solution of dp[i] include at least 2 numbers
    # for example dp[4]=3  dp[7]=3*4=12, but 4>dp[4]
    # Time: O(n)<~<O(n^2)
    # Space: O(n)
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            for j in range(i-1,0,-1):
                dp[i]=max(dp[i],j*dp[i-j],j*(i-j))
        return dp[-1]


if __name__=='__main__':
    print(Solution().integerBreak(
        10
    ))