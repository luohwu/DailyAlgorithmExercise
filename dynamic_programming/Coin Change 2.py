# https://leetcode.com/problems/coin-change-2/


from typing import List

# one solution: just return the numbers of result of the problem 'combination sum'
# https://leetcode.com/problems/combination-sum/

# here we use dynamic_programming method


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coint in coins:
            for i in range(1,amount+1):
                if i>=coint:
                    dp[i]+=dp[i-coint]
        return dp[-1]