# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid
        return  -1

if __name__=='__main__':
    print(Solution().search(
        nums = [-1,0,3,5,9,12], target = 2
    ))
