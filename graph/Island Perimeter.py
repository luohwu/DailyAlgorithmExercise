# https://leetcode.com/problems/island-perimeter/

from typing import List
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=[[False]*cols for i in range(rows)]
        min_row=rows+1
        max_row=-1
        min_col=cols+1
        max_col=-1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    queue=deque([(row,col)])
                    visit[row][col]=True
                    while queue:
                        cur_row,cur_col=queue.pop()

                        min_row=min(min_row,cur_row)
                        max_row=max(max_row,cur_row)
                        min_col=min(min_col,cur_col)
                        max_col=max(max_col,cur_col)
                        for move_row,move_col in [(-1,0),(1,0),(0,1),(0,-1)]:
                            new_row=cur_row+move_row
                            new_col=cur_col+move_col
                            if new_row>-1 and new_row<rows and new_col>-1 and new_col<cols and visit[new_row][new_col]==False and \
                                grid[new_row][new_col]==1:
                                queue.append((new_row,new_col))
                                visit[new_row][new_col]=True
                    break
        print
        return  2*(max_row-min_row+1+max_col-min_col+1)


if __name__=='__main__':
    print(Solution().islandPerimeter(
        grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    ))




