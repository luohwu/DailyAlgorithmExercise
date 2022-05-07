# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(board,row,col,word):
            nonlocal visit_table
            if len(word)==0:
                return True
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]) or board[row][col]!=word[0] or visit_table[row][col]==1:
                return False

            visit_table[row][col]=1
            flag= search(board,row+1,col,word[1:]) or search(board,row-1,col,word[1:]) or search(board,row,col-1,word[1:]) \
                   or search(board,row,col+1,word[1:])

            # it's important to set the visit value back to 0
            visit_table[row][col]=0
            return flag


        m,n=len(board),len(board[0])
        visit_table=[[0]*n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if search(board,row,col,word):
                    return True

        return False


if __name__=='__main__':
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"ABCB"))
