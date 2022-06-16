# https://leetcode.com/problems/combination-sum/
from typing import List
class Solution:


    #   update!!!!!!!!!!!!!!!
    #   looks like this method results in Memory limit Exceeded now
    def combinationSumOld(self, candidates: List[int], target: int) -> List[List[int]]:
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


    # still recursive method
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def search(candidates:List,target:int, path):
            if target<0:
                return
            if target==0:
                res.append(path)
                return

            # avoid redundant computation here using candidates[idx:] instead of the whole candidates
            for idx,num in enumerate(candidates):
                search(candidates[idx:],target-num,path+[num])
        search(candidates,target,[])
        return res

if __name__=='__main__':
    print(Solution().combinationSum(

        candidates=[2, 3, 6, 7], target=7
    ))
