# https://leetcode.com/problems/pacific-atlantic-water-flow/

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        result = []
        visit=[]
        for r in range(n):
            for c in range(m):
                queue = deque([[r, c]])
                pacific = False
                atlantic = False
                visit=[]
                while queue:
                    cur_r, cur_c = queue.popleft()
                    visit.append([cur_r,cur_c])
                    #up
                    if cur_r - 1 < 0:
                        pacific = True
                    elif heights[cur_r - 1][cur_c] <= heights[cur_r][cur_c] and [cur_r-1,cur_c] not in visit:
                        queue.append([cur_r - 1, cur_c])

                    #left
                    if cur_c - 1 < 0:
                        pacific = True
                    elif heights[cur_r][cur_c - 1] <= heights[cur_r][cur_c] and [cur_r,cur_c-1] not in visit:
                        queue.append([cur_r, cur_c - 1])

                    #down
                    if cur_r + 1 >= n:
                        atlantic = True
                    elif heights[cur_r + 1][cur_c] <= heights[cur_r][cur_c] and [cur_r+1,cur_c] not in visit:
                        queue.append([cur_r + 1, cur_c])

                    #right
                    if cur_c + 1 >= m:
                        atlantic = True
                    elif heights[cur_r][cur_c + 1] <= heights[cur_r][cur_c] and [cur_r,cur_c+1] not in visit:
                        queue.append([cur_r, cur_c + 1])
                if pacific and atlantic:
                    result.append([r, c])
        return result
if __name__=='__main__':
    print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))