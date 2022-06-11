# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    # Time: O(log n)
    # Space: O(1) beats 92.79%
    # apply a normal binary search
    # if target is in nums
    # search forward and backward to find the first position and last position
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        n=right=len(nums)
        found=False
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                found=True
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid

        # if target is not in nums
        if not found:
            return [-1,-1]


        # search in both directions starting from mid
        first=mid
        last=mid
        while first-1>=0 and nums[first-1]==target:
            first-=1
        while last+1<n and nums[last+1]==target:
            last+=1
        return [first,last]

if __name__=='__main__':
    print(Solution().searchRange(
        nums = [5,7,7,8,8,10], target = 6
    ))
