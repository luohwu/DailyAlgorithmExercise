# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:

    # dynamic programming
    # 'dp' is our table, with dp[i] indicates the maximum sum of subarray that involves nums[i]
    # Time O(n)
    # Space O(n) beats 96.35% of other submissions
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[nums[0]]*n
        for i in range(1,n):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
        return max(dp)

if __name__=='__main__':
    print(Solution().maxSubArray(
        nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ))