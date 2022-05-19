# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            x,y=point
            heapq.heappush(heap,(x*x+y*y,point))
        result=[]
        while k>0:
            _,point=heapq.heappop(heap)
            result.append(point)
            k-=1
        return result

if __name__=='__main__':
    print(Solution().kClosest(
        points=[[3, 3], [5, -1], [-2, 4]], k=2
    ))
