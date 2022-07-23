# https://leetcode.com/problems/island-perimeter/

from typing import List
from collections import deque

class Solution:
    # Both DFS and BFS can work here
    # search from the first '1'
    # initial result =0 (Perimeter =0)
    # in each searching iteration, res+=1 if not adding the node to the queue, otherwise just normal search
    # Time: O(row*col)
    # Space: same
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=[[False]*cols for i in range(rows)]
        res=0

        for row in range(rows):
            for col in range(cols):

                # find the first island
                if grid[row][col]==1:
                    queue=deque([(row,col)])
                    visit[row][col]=True
                    while queue:
                        cur_row,cur_col=queue.pop()
                        for move_row,move_col in [(-1,0),(1,0),(0,1),(0,-1)]:
                            new_row=cur_row+move_row
                            new_col=cur_col+move_col

                            # two situation here
                            # if is the node we are going to explore
                            if new_row>-1 and new_row<rows and new_col>-1 and new_col<cols and  grid[new_row][new_col]==1:
                                if visit[new_row][new_col]==False:
                                    queue.append((new_row, new_col))
                                    visit[new_row][new_col] = True
                            # edge case, res+=1
                            else:
                                res+=1
                    return res

if __name__=='__main__':
    print(Solution().islandPerimeter(
        grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    ))




