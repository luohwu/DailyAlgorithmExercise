# https://leetcode.com/problems/01-matrix/

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        movements=[[-1,0],[1,0],[0,-1],[0,1]]
        rows,cols=len(mat),len(mat[0])
        visit=[[False]*cols for i in range(rows)]
        result=[[-1]*cols for i in range(rows)]
        queue=deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]==0:
                    result[row][col]=0
                    queue.append([row,col])
                    visit[row][col]=True
        while queue:
            row,col=queue.popleft()
            for movement in movements:
                new_row,new_col=row+movement[0],col+movement[1]
                if new_row>=0 and new_row<rows and new_col>=0 and new_col<cols and visit[new_row][new_col]==False:
                    result[new_row][new_col]=result[row][col]+1
                    visit[new_row][new_col]=True
                    queue.append([new_row,new_col])
        return result






if __name__=='__main__':
    print(Solution().updateMatrix(
        [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]

    ))








