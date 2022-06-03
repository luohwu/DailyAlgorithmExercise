# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """

        # modify nums1 from the end to the start

        # if there is still elements in nums2
        while n>0:

            # choose element in nums1
            if nums1[m-1]>nums2[n-1] and m>0:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            # choose element in nums2
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1