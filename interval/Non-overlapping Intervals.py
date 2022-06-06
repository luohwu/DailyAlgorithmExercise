# https://leetcode.com/problems/non-overlapping-intervals/

from typing import  List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        s,e=intervals[0]
        res=0
        for new_s,new_e in intervals[1:]:
            if new_s<e:
                e=min(e,new_e)
                res+=1
            else:
                e=new_e
        return res

if __name__=='__main__':
    print(Solution().eraseOverlapIntervals(
        [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    ))
