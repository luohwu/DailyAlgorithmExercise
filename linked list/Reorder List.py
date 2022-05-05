# https://leetcode.com/problems/reorder-list/

from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        table=dict()
        num=-1
        while(head):
            num+=1
            table[num]=head
            head=head.next
        left_size=int(num/2)
        for left_idx in range(left_size+1):
            if left_idx>0:
                table[num-left_idx+1].next=table[left_idx]
            right_idx=num-left_idx
            if left_idx==right_idx:
                table[left_idx].next=None
            else:
                table[left_idx].next=table[right_idx]
                table[right_idx].next=None