# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List
class Solution:
    # simple dp
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i]+=dp[i-1]
        return max(dp)


