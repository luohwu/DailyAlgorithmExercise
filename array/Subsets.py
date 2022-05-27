# https://leetcode.com/problems/subsets/
from typing import List

class Solution:

    # very simple solution... beat 99.32% lol
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            res=res+[[num]+item for item in res]
        return res

if __name__=='__main__':
    print(Solution().subsets([1,2,3]))