# https://leetcode.com/problems/majority-element/

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        table=dict()
        for num in nums:
            if num not in table.keys():
                table[num]=1
                if table[num]>int(n/2):
                    return num
            else:
                table[num]+=1
                if table[num]>int(n/2):
                    return num
