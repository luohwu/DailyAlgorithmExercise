# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:

    # Time: O(log n)
    # Space: O(1)
    # just be careful of the edge cases <=nums[0] or >=nums[end]
    def searchInsert(self, nums: List[int], target: int) -> int:
        right=len(nums)
        left=0
        if target<nums[0]:
            return 0
        if target>nums[right-1]:
            return right
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=target and nums[mid-1]<target:
                return mid
            elif nums[mid]>target:
                right=mid
            else:
                left=mid+1


if __name__=='__main__':
    print(Solution().searchInsert(
        nums=[1, 3, 5, 6], target=0
    ))
