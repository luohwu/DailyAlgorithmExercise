# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def search(current_sum, idx):
            nonlocal target, n
            if current_sum == target:
                return True
            if current_sum > target or idx >= n:
                return False
            return search(current_sum + nums[idx], idx + 1) or search(current_sum, idx + 1)

        n = len(nums)
        total_sum = sum(nums)
        target = total_sum // 2
        if total_sum % 2 == 1:
            return False
        return search(0, 0)

if __name__=='__main__':
    print(Solution().canPartition(

        [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
    ))
