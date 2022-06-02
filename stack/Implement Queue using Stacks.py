# https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque
class MyQueue:

    def __init__(self):
        self.stack1=deque()
        self.stack2=deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    # assume you have 2 cups A and B
    # to take out the bottom item in A, pour items in A to B
    # the top item in B is the target item
    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        result=self.stack2.pop()
        while self.stack2.pop():
            self.stack1.append(self.stack2.pop())
        return result

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        result=self.stack2.pop()
        self.stack1.append(result)
        while self.stack2.pop():
            self.stack1.append(self.stack2.pop())
        return result

    def empty(self) -> bool:
        return len(self.stack1)==0