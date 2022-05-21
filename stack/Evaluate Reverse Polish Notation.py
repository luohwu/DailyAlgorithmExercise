# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue=deque()
        operators=['+','-','*','/']
        operations={
            '+': lambda x,y: x+y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: int(x * y),
            '/': lambda x, y: int(x / y),
        }
        for item in tokens:
            if item not in operators:
                queue.append(int(item))
            else:
                second_operand=queue.pop()
                first_operand=queue.pop()
                queue.append(operations[item](first_operand,second_operand))
        return queue.pop()

if __name__=='__main__':
    print(Solution().evalRPN(
        ["4","13","5","/","+"]
    ))