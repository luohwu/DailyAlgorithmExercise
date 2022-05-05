# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        row,col=0,-1
        visit_table=[[0]*n for i in range(m)]

        res=[]
        while(len(res)<m*n):
            #move right
            while(col+1<n and visit_table[row][col+1]==0):
                col+=1
                res.append(matrix[row][col])
                visit_table[row][col]=1
            #move down
            while (row+1<m and visit_table[row+1][col]==0):
                row+=1
                res.append(matrix[row][col])
                visit_table[row][col]=1
            #move left
            while(col-1>=0 and visit_table[row][col-1]==0):
                col-=1
                res.append(matrix[row][col])
                visit_table[row][col]=1
            #move up
            while(row-1>=0 and visit_table[row-1][col]==0):
                row-=1
                res.append(matrix[row][col])
                visit_table[row][col]=1

        return res

if __name__=='__main__':
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))