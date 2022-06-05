# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # sort all intervals first
        points=sorted(points)
        # print(points)
        arrows=1
        s,e=points[0]

        # just track the frontest end
        for new_s,new_e in points[1:]:
            if new_s>e:
                e=new_e
                arrows+=1
            else:
                e=min(e,new_e)
        return  arrows




if __name__=='__main__':
    print(Solution().findMinArrowShots(
        [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    ))
