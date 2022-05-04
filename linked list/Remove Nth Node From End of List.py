# https://leetcode.com/problems/reverse-linked-list/

from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num=-1
        table=dict()
        while(head):
            num+=1
            table[num] = ListNode(val=head.val, next=None)
            if num>0:
                table[num-1].next=table[num]

            head=head.next
        if num==0:
            return None
        idx_to_remove=num-n+1
        # print(idx_to_remove)
        if idx_to_remove==0:
            return table[1]

        if idx_to_remove==num:
            table[num-1].next=None
        else:
            table[idx_to_remove - 1].next = table[idx_to_remove + 1]
        print(table[idx_to_remove-1])
        return table[0]

