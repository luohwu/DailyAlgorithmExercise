# https://leetcode.com/problems/assign-cookies/

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g,reverse=True)
        s=sorted(s,reverse=True)
        length_g=len(g)
        length_s=len(s)
        index_g=0
        index_s=0
        res=0
        while index_g<length_g and index_s<length_s:
            if s[index_s]>=g[index_g]:
                res+=1
                index_s+=1
                index_g+=1
            else:
                index_g+=1
        return res