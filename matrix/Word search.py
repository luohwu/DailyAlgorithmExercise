# https://leetcode.com/problems/word-search/

from typing import List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        for row in range(m):
            for col in range(n):
                #search from each position
                if board[row][col]==word[0]:
                    visit_table=[[0]*n for i in range(m)]
                    visit_table[row][col]=1
                    queue=deque([row,col,visit_table])
                    while queue:
                        current_row,current_col,current_visit_table=deque.popleft()
                        #TBD

