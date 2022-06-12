# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    # m, n= #rows, #cols
    # Time: O(log max(m,n))
    # Space: O(m)
    # just apply binary search twice
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # apply a binary search on the first col to find the target row ( which row the target is in)
        first_col=[row[0] for row in matrix]
        up=0
        bottom=len(first_col)
        m,n=len(matrix),len(matrix[0])
        while up<bottom:
            mid=(up+bottom)//2
            if first_col[mid]==target or (mid+1<m and first_col[mid]<target and first_col[mid+1]>target):
                break
            elif first_col[mid]<target:
                up=mid+1
            else:
                bottom=mid
        target_row=matrix[mid]

        # apply a second binary search on the target row to find the exact position
        # return False if target is not in the target row
        left=0
        right=len(target_row)
        while left<right:
            mid=(left+right)//2
            if target_row[mid]==target:
                return True
            elif target_row[mid]<target:
                left=mid+1
            else:
                right=mid
        return False


if __name__=='__main__':
    print(Solution().searchMatrix(
        matrix = [[1],[3]], target = 3
    ))
