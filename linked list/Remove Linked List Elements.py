# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=dummy_link=ListNode()
        while head:
            if head.val!=val:
                dummy_link.next=head
                dummy_link=dummy_link.next
            head=head.next
        dummy_link.next=None
        return dummy_head.next
