# https://leetcode.com/problems/wiggle-subsequence/

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # remove redundant num in nums
        # because they are useless and can be deleted directly
        digit=[]
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                digit.append(nums[i])
        digit.append(nums[-1])
        nums=digit


        # special case
        if len(nums)<2:
            return len(nums)

        # construct the difference array
        difference=[]
        for i in range(1,len(nums)):
            difference.append(nums[i]-nums[i-1])

        # just traverse the difference array
        res=0
        for idx in range(1,len(difference)):
            if difference[idx]*difference[idx-1]<0:
                res+=1

        return res+2

if __name__=='__main__':
    print(Solution().wiggleMaxLength(
        [0,0,0]
    ))
