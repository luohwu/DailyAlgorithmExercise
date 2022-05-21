# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=[[False]*cols for i in range(rows)]
        queue=deque()
        movements=[[-1,0],[1,0],[0,-1],[0,1]]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    # dont visit empty grid in the future
                    visit[row][col]=True
                elif grid[row][col]==2:
                    visit[row][col]=True
                    queue.append([row,col])
        # if there are still rotten oranges in the queue
        while queue:
            row,col=queue.popleft()

            #traverse neighbors
            for row_move,col_move in movements:
                row_new,col_new=row+row_move,col+col_move
                if row_new>=0 and row_new<rows and col_new>=0 and col_new<cols and visit[row_new][col_new]==False:
                    grid[row_new][col_new]=grid[row][col]+1
                    queue.append([row_new,col_new])
                    visit[row_new][col_new]=True

        # the value of rotten oranges is 2
        result=2
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    # fial, since there is still a fresh orange
                    return -1
                else:
                    result=max(result,grid[row][col])
        return result-2


if __name__=='__main__':
    print(Solution().orangesRotting(
        [[0,1,2]]
    ))




