# https://leetcode.com/problems/01-matrix/

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        movements=[[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(row_start,col_start):
            visit=[]
            queue=deque([[row_start,col_start]])

            while queue:
                row,col=queue.popleft()
                visit.append([row,col])
                if row<0 or row>=m or col<0 or col>=n:
                    continue
                if mat[row][col]==0:
                    row_end=row
                    col_end=col
                    break
                else:
                    for row_move,col_move in movements:
                        row_new=row+row_move
                        col_new=col+col_move
                        if [row_new,col_new] not in visit:
                            queue.append([row_new,col_new])
            return abs(row_end-row_start)+abs(col_end-col_start)





        m,n=len(mat),len(mat[0])
        result=[[0]*n for i in range(m)]
        for row in range(m):
            for col in range(n):
                result[row][col]=bfs(row,col)
        return result


if __name__=='__main__':
    print(Solution().updateMatrix(

        [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]
    ))








