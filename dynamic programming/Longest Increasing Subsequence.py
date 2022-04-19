#https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        res=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    res[i]=max(res[i],res[j]+1)
        print(res)
        return max(res)