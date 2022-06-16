# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # just be careful with the corner case, num==1
        # otherwise, is an application of binary search
        if num==1:
            return True
        left=0
        right=num
        while left<right:
            mid=(left+right)//2
            mid_square=mid*mid
            if mid_square==num:
                return True
            elif mid_square>num:
                right=mid
            else:
                left=mid+1
