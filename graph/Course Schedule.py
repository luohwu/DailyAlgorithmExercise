# https://leetcode.com/problems/course-schedule/

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue=deque()
        taken=[]
        high_level_course=[course[0] for course in prerequisites]
        table=[[] for i in range((numCourses+1))]
        for i in range(numCourses):
            if i not in high_level_course:
                taken.append(i)
                queue.append(i)
        for prerequisity in prerequisites:
            table[prerequisity[0]].append(prerequisity[1])
        while queue:
            cur_course=queue.popleft()
            for prerequisity in prerequisites:
                if prerequisity[1]==cur_course and prerequisity[0] not in taken and all(a in taken for a in table[prerequisity[0]]):
                    queue.append(prerequisity[0])
                    taken.append(prerequisity[0])
        return True if len(taken)==numCourses else False

if __name__=='__main__':
    print(Solution().canFinish(3,[[1,4],[2,4],[3,1],[3,2]]))