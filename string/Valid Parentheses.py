# https://leetcode.com/problems/valid-parentheses/
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        right_brackets=[')','}',']']
        left_brackets=['(','{','[']
        queue=deque()

        for char in s:
            if char in left_brackets:
                queue.append(char)
            if char in right_brackets:
                if len(queue)==0:
                    return False
                cur_left = queue.pop()
                if left_brackets.index(cur_left)!=right_brackets.index(char):
                    return False

        return len(queue)==0







if __name__=='__main__':
    print(Solution().isValid(
        s = "([])"
    ))