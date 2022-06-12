# https://leetcode.com/problems/valid-triangle-number/

from typing import List


class Solution:
    #Time: O(n^2)
    # Space: O(n) because of sorted()
    def triangleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        res=0
        for right in range(2,n):
            left=0
            mid=right-1
            while left<mid:
                if nums[left]+nums[mid]>nums[right]:
                    res+=mid-left
                    mid-=1
                else:
                    left+=1
        return res

if __name__=='__main__':
    print(Solution().triangleNumber(
        nums=[2, 2, 3, 4]
    ))