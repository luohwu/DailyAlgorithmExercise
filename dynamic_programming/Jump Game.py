# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        for i in range(1, length):
            for j in range(1, i + 1):
                if dp[i - j] > 0 and j <= nums[i-j]:
                    dp[i] += dp[i - j]
                    break
            # can't jump to i-th index
            return False
        return dp[-1]


if __name__=='__main__':
    print(Solution().canJump([2,3,1,1,4]))