# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 0 node or 1 node
        # just return head
        if not head or not head.next:
            return head

        # two sub links
        odd_head=odd_link=head
        even_head=even_link=head.next

        # process two nodes at each time step
        while even_link.next and even_link.next.next:
            odd_link.next=even_link.next
            odd_link=odd_link.next
            even_link.next=even_link.next.next
            even_link=even_link.next

        # two cases:
        # case 1: there is still one node
        if even_link.next:
            odd_link.next=even_link.next
            # concatenate the odd link and the even link
            odd_link.next.next=even_head
            even_link.next=None
            return odd_head
        # case 2: there is no node left
        else:
            odd_link.next=even_head
            return odd_head