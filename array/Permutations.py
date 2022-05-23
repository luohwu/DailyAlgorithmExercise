# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n==0:
            return [[]]
        result=[]

        #just recursion over all elements
        for idx in range(n):
            result += [[nums[idx]] + item for item in self.permute(nums[0:idx] + nums[idx + 1:])]
        return result

if __name__=='__main__':
    print(Solution().permute(
        [1,2,3]
    ))



