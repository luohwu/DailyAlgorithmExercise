# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import deque
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)

        visit=[]
        max_num=0
        for num in nums:
            if num not in visit:
                queue=deque([num])
                num_conce=0
                visit.append(num)
                while queue:
                    cur_num=queue.popleft()
                    num_conce+=1
                    for new_num in [cur_num-1,cur_num+1]:
                        if new_num not in visit and new_num in nums:
                            queue.append(new_num)
                            visit.append(new_num)
                max_num=max(num_conce,max_num)
        return max_num

    #simple method
    # remember set is faster than List
    def longestConsecutiveSimple(self, nums: List[int]) -> int:
        # nums=set(nums)
        set=set(nums)
        max_num=0
        for num in nums:
            temp_num=1
            #smaller direction
            smaller_num=num-1
            while smaller_num in set:
                set.remove(smaller_num)
                temp_num+=1
                smaller_num-=1
            greater_num=num+1
            while greater_num in set:
                set.remove(greater_num)
                temp_num+=1
                greater_num+=1
            max_num=max(max_num,temp_num)