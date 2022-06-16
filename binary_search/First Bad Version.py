# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


# just binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=0
        right=n+1
        while left<right:
            mid=(left+right)//2
            if mid>0 and isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return mid


