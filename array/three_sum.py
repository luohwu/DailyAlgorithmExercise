# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n==0:
            return []
        nums=sorted(nums)

        idx_first_positive=0
        nums_zero=0
        while nums[idx_first_positive]<=0:
            if nums[idx_first_positive]==0:
                nums_zero+=1
            idx_first_positive+=1
            if idx_first_positive==n:
                if nums_zero>=3:
                    return [[0,0,0]]
                else:
                    return []
        result=[]
        for l_idx in range(idx_first_positive+1):
            for r_idx in range(idx_first_positive,n):
                complement = -nums[l_idx] - nums[r_idx]
                if complement in nums[l_idx + 1:r_idx] and [nums[l_idx], complement, nums[r_idx]] not in result:
                    result.append([nums[l_idx], complement, nums[r_idx]])
        if nums_zero>=3:
            result.append([0,0,0])
        return result

if __name__=='__main__':
    print(Solution().threeSum(
        nums=[-2, 1,1]
    ))

