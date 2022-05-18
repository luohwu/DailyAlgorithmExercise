# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ok this is a very easy problem....
        table=[]
        while head:
            table.append(head)
            head=head.next
        n=len(table)
        return table[int(n/2)]
