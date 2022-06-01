# https://leetcode.com/problems/partition-list/

from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        buffer = []
        first = head
        second = head.next

        #buffer all nodes with node.val<x
        while second:
            # print(second.val)
            if second.val < x:
                buffer.append(second)
                first.next = second.next
                second = second.next
            else:
                first = first.next
                second = second.next

        if not buffer:
            return head
        print(buffer)

        # the head of the new link of the buffered nodes
        head_new_branch = buffer.pop(0)
        tail_new_branch = head_new_branch

        # construct the new link
        while buffer:
            tail_new_branch.next = buffer.pop(0)
            tail_new_branch = tail_new_branch.next

        # two cases
        if head.val < x:
            temp = head.next
            head.next = head_new_branch
            tail_new_branch.next = temp
            return head
        else:
            tail_new_branch.next = head
            return head_new_branch



