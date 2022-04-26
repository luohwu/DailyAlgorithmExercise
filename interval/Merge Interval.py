# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key=lambda item:item[0])
        current_interval=intervals[0]
        for interval in intervals[1:]:
            if (current_interval[1]<=interval[1] and current_interval[1]>=interval[0]) or \
                    (current_interval[0]<=interval[1] and current_interval[0]>=interval[0]) or \
                    (current_interval[0]<interval[0] and current_interval[1]>interval[1]):
                current_interval[0]=min(current_interval[0],interval[0])
                current_interval[1]=max(current_interval[1],interval[1])
            else:
                result.append(current_interval)
                current_interval=interval
        result.append(current_interval)
        return result


if __name__=='__main__':
    print(Solution().merge(
        [[2,3],[4,5],[6,7],[8,9],[1,10]]
    ))