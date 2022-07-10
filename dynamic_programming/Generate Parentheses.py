# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    # generateParenthesis(n) is generated from generateParenthesis(n-1)

    def generateParenthesis(self, n: int) -> List[str]:
        res={""}
        for i in range(n):
            temp=set([])
            for item in res:
                l=len(item)
                for intert_idx in range(l):
                    temp.add(item[:intert_idx]+"()"+item[intert_idx:])
                temp.add(item+"()")
            res=temp
        return res