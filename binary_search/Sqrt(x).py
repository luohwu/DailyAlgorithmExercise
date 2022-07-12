# https://leetcode.com/problems/sqrtx/

class Solution:
    # be careful with the ending condition
    # Time: O(logn)
    # Space: O(1)
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left=0
        right=x+1
        while left<right:
            mid=(left+right)//2
            mid_square=mid*mid
            temp=(mid+1)*(mid+1)

            # two situations:
            # a) 2*2=4
            # b) 2*2<8 but 3*3>9
            if mid_square==x  or (mid_square<x and temp>x):
                return mid
            elif mid_square<x:
                left=mid+1
            else:
                right=mid
        return -1

if __name__=='__main__':
    print(Solution().mySqrt(1))