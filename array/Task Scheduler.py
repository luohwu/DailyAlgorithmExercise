# https://leetcode.com/problems/task-scheduler/

from typing import List
class Solution:
    # the key is to sort tasks according to their times
    # process first the tasks with more remaining times
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result=0
        remaining_tasks=[0]*26
        for task in tasks:
            remaining_tasks[ord(task)-ord('A')]+=1
        remaining_tasks=[item for item in remaining_tasks if item >0]
        remaining_tasks=sorted(remaining_tasks,reverse=True)
        while remaining_tasks:
            # special case for the last cycle
            # for example, if the remaining task is [A:1,B:1], it just takes 2 time units to finish the remaining task
            if len(remaining_tasks)==sum(remaining_tasks) and len(remaining_tasks)<=n+1:
                result+=len(remaining_tasks)
            # normal case, it always takes n+1 time unites to finish one cycle
            else:
                result+=(n+1)

            kinds_remained_tasks=len(remaining_tasks)
            # need idle
            if kinds_remained_tasks<=n:
                # new remaining_task set
                # remove task if num(task)<=0
                remaining_tasks=[item-1 for item in remaining_tasks if item>1]
            # no need idle
            else:
                temp=[]
                for idx,item in enumerate(remaining_tasks):
                    # only process the first n+1 tasks
                    if idx<n+1:
                        if item>1:
                            temp.append(item-1)
                    else:
                        temp.append(item)
                # the order may change, so need to sort again
                remaining_tasks=sorted(temp,reverse=True)
        return result





if __name__=='__main__':
    print(Solution().leastInterval(
        tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
    ))
