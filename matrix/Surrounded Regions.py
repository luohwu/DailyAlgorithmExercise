# https://leetcode.com/problems/surrounded-regions/
from typing import List
from collections import deque


class Solution:
    # search from elements on the boarder, both DFS and BFS will work
    # time: O(rows*cols)
    # space: same
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])

        # if the final result should be 'O' or not, initialized with False
        final_O=[[False]*cols for i in range(rows)]
        visit=[[False]*cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                # only consider 'O' on the boarder
                if row==0 or row==rows-1 or col==0 or col==cols-1:
                    if board[row][col]=='O':

                        # start searching all neighboring 'O', which should be remained in the end
                        queue=deque([(row,col)])
                        visit[row][col]=True
                        final_O[row][col] = True
                        while queue:
                            cur_row,cur_col=queue.popleft()
                            # final_O[cur_row][cur_col]=True
                            for move in [(-1,0),(+1,0),(0,-1),(0,1)]:
                                new_row=cur_row+move[0]
                                new_col=cur_col+move[1]
                                if new_row>=0 and new_row<rows and new_col>=0 and new_col<cols and board[new_row][new_col]=='O'\
                                        and visit[new_row][new_col]==False:
                                    queue.append((new_row,new_col))
                                    visit[new_row][new_col]=True
                                    final_O[new_row][new_col] = True

        #modify board according to seaching result
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='O' and final_O[row][col]==False:
                    board[row][col]='X'

if __name__=='__main__':
    print(Solution().solve(
        board=[["X", "O", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    ))



