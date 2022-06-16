# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import List

# application of binary search
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)
        while left<right:
            mid=(left+right)//2
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid-1]:
                right=mid
            else:
                left=mid+1

