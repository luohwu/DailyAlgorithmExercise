# https://leetcode.com/problems/coin-change-2/


from typing import List

# one solution: just return the numbers of result of the problem 'combination sum'
# https://leetcode.com/problems/combination-sum/

# here we use dynamic programming method


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #TBD