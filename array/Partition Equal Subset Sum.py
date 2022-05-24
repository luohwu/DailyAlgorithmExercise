# https://leetcode.com/problems/partition-equal-subset-sum/

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
            for idx,num in enumerate(candidates):
                if num<target:
                    #recursion here
                    result=result+[[num]+item for item in search(candidates[0:idx]+candidates[idx+1:],target-num)]
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

    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        combination=self.combinationSum(nums,total_sum/2)
        # print(combination)
        if len(combination)>0:
            return True
        else:
            return False

if __name__=='__main__':
    print(Solution().canPartition(

        [1,2,5]
    ))
