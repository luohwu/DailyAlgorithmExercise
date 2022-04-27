# https://leetcode.com/problems/reverse-linked-list/

from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        table=dict()
        while head:
            if head in table:
                return True
            else:
                table[head]=1
                head=head.next
        return False




