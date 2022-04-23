# https://leetcode.com/problems/pacific-atlantic-water-flow/

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        queue_pacific=deque()
        queue_atlantic=deque()
        pacific=[[0]*n for r in range(m)]
        atlantic=[[0]*n for r in range(m)]
        visit_pacific=[]
        visit_atlantic=[]
        for r in range(m):
            for c in range(n):
                if r==0 or c==0:
                    queue_pacific.append([r,c])
                    visit_pacific.append([r, c])
                if r==m-1 or c==n-1:
                    queue_atlantic.append([r,c])
                    visit_atlantic.append([r, c])
        # consider pacific first
        while queue_pacific:
            cur_r,cur_c=queue_pacific.popleft()
            pacific[cur_r][cur_c]=1
            for move_r,move_c in [[-1,0],[0,-1],[+1,0],[0,1]]:
                new_r=cur_r+move_r
                new_c=cur_c+move_c
                # new position is within range, heigher than cur position, and not visited before
                if new_r>-1 and new_r<m and new_c>-1 and new_c<n and heights[new_r][new_c]>=heights[cur_r][cur_c] and\
                        [new_r,new_c] not in visit_pacific:
                    queue_pacific.append([new_r,new_c])
                    visit_pacific.append([new_r, new_c])
        # consider atlantic
        while queue_atlantic:
            cur_r,cur_c=queue_atlantic.popleft()
            atlantic[cur_r][cur_c]=1
            visit_atlantic.append([cur_r,cur_c])
            for move_r,move_c in [[-1,0],[0,-1],[+1,0],[0,1]]:
                new_r=cur_r+move_r
                new_c=cur_c+move_c
                if new_r>-1 and new_r<m and new_c>-1 and new_c<n and heights[new_r][new_c]>=heights[cur_r][cur_c] and\
                        [new_r,new_c] not in visit_atlantic:
                    queue_atlantic.append([new_r,new_c])
                    visit_atlantic.append([new_r, new_c])
        result=[]
        for r in range(m):
            for c in range(n):
                if atlantic[r][c]==1 and pacific[r][c]==1:
                    result.append([r,c])

        return result
if __name__=='__main__':
    print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))