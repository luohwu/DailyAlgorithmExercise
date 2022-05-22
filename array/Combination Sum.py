# https://leetcode.com/problems/combination-sum/
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive method
        # solve sub-problems
        candidates=sorted(candidates)

        def search(candidates:List[int],target:int):
            #avoid re-computation
            nonlocal table
            if target in table.keys():
                return table[target]
            result=[]
            for num in candidates:
                if num<target:
                    #recursion here
                    result=result+[[num]+item for item in search(candidates,target-num)]
                elif num==target:
                    return result+[[num]]
            table[target]=result
            return result
        table=dict()
        # raw result, including redundant combinations
        tmp=search(candidates,target)
        sorted_temp=[sorted(item) for item in tmp]
        # return sorted_temp

        result=[]
        for item in sorted_temp:
            if item not in result:
                result.append(item)
        return result

if __name__=='__main__':
    print(Solution().combinationSum(

        [2, 7, 6, 3, 5, 1],
    9
    ))
