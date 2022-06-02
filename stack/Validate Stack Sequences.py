# https://leetcode.com/problems/validate-stack-sequences/

from typing import List
from collections import deque
class Solution:

    # just create a stack
    # if popped[idx_pop] not in stack, push new element to stack
    # if popped[idx_pop] in stack, check if popped[idx_pop]==stack.pop()
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=deque()
        idx_push=0
        idx_pop=0
        while idx_pop<len(popped):
            if popped[idx_pop] not in stack:
                if idx_push==len(pushed):
                    return False
                stack.append(pushed[idx_push])
                idx_push+=1

            else:
                if stack.pop()==popped[idx_pop]:
                    idx_pop+=1
                else:
                    return False
        return True

if __name__=='__main__':
    print(Solution().validateStackSequences(
        pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]
    ))
