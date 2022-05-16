# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from typing import List,Optional



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table=dict()
        for num in nums:
            if num in table.keys():
                table[num]+=1
            else:
                table[num]=1
        heap=[]
        for number,freq in table.items():
            heap.append((-freq,number))
        heapq.heapify(heap)
        res=[]

        while k>0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res


if __name__=='__main__':
    print(Solution().topKFrequent(

        [3, 0, 1, 0],
    1
    ))
