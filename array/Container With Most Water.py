# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:

    # consider the length of the bottom
    # shrink the bottom from maximum to minimum

    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        areas=[]
        while right>left:
            if height[left]<height[right]:
                areas.append((right-left)*height[left])
                left+=1
            else:
                areas.append((right-left)*height[right])
                right-=1
        return max(areas)



