# https://leetcode.com/problems/reverse-linked-list/

from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=deque([head])
        while head.next:
            stack.append(head.next)
            head=head.next
        reversed_head=stack.pop()
        current_node=reversed_head
        while stack:
            node=stack.pop()
            node.next=None
            current_node.next=node
            current_node=current_node.next
        return reversed_head




