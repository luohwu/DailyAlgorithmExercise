# https://leetcode.com/problems/insert-interval/
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval, *intervals]
        new_start,new_end=newInterval
        idx_start=-1
        idx_end=-1
        for idx,interval in enumerate(intervals):

            #analyze different situations for start and end value
            if interval[1]<new_start:
                idx_start+=1
            if new_start>=interval[0] and new_start<=interval[1]:
                new_start=interval[0]
                # idx_start+=1
                # idx_start+=1

            if new_end>=interval[0] and new_end<=interval[1]:
                new_end=interval[1]
                idx_end+=1
            if new_end>interval[1]:
                idx_end+=1
        result=[*intervals[:idx_start+1],[new_start,new_end],*intervals[idx_end+1:]]
        return result

if __name__=='__main__':
    print(Solution().insert(
        intervals = [[1,5]], newInterval = [6,9]
    ))