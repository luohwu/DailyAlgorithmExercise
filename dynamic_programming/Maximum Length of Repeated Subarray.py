# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

from typing import List


class Solution:
    # dp with dp[i][j] means the maximum length of repeated subarray of nums1[:i] and nums2[:j]
    # note that nums1[i] and nums2[j] must be ending of each subarray
    # Time O(len(nums1)*len(nums2))
    # Space: same
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        rows=len(nums1)
        cols=len(nums2)
        dp=[[0]*cols for i in range(rows)]
        for col in range(cols):
            dp[0][col]=1 if nums1[0]==nums2[col] else 0
        for row in range(rows):
            dp[row][0]=1 if nums1[row]==nums2[0] else 0
        for row in range(1,rows):
            for col in range(1,cols):
                if nums1[row]==nums2[col]:
                    dp[row][col]=1+dp[row-1][col-1]
        return max([item for row in dp for item in row])

if __name__=='__main__':
    print(Solution().findLength(
        [1, 2, 3, 2, 1],
        [3, 2, 1, 4, 7]
    ))