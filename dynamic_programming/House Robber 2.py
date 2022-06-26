# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 3:
            return max(nums)
        # rob house 0
        dp_with0 = [0] * length
        # not rob house 0
        dp_without0 = [0] * length
        dp_with0[0] = nums[0]
        dp_with0[1] = nums[0]
        dp_with0[2] = nums[0]
        for i in range(3, length):
            dp_with0[i] = max(dp_with0[i - 2] + nums[i - 1], dp_with0[i - 1])
        dp_without0[0] = nums[0]
        dp_without0[1] = nums[1]
        dp_without0[2] = max(nums[1], nums[2])
        for i in range(3, length):
            dp_without0[i] = max(dp_without0[i - 2] + nums[i], dp_without0[i - 1])

        return max(dp_with0 + dp_without0)

if __name__=='__main__':
    print(Solution().rob([4,1,2,7,5,3,1]))