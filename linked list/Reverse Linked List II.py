# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head

        # 1-indexed to 0-indexed
        left=left-1
        right=right-1

        # construct 3 links, front, middle, back
        # the final result is front->middle->back
        # before concatenate them, need to reverse middle first
        front_head=front=ListNode()
        # to reverse middle, use a queue to buffer nodes in middle
        middle_queue=[head]*(right-left+1)
        back_head=back=ListNode()
        idx=0
        while head:
            # nodes of the front
            if idx<left:
                front.next=head
                front=front.next
            # nodes of the back
            elif idx>right:
                back.next=head
                back=back.next
            # nodes of the middle
            # buffer first
            else:
                middle_queue[idx-left]=head
            idx+=1
            head=head.next

        # reverse the middle link
        middle_head=middle=ListNode()
        idx=right-left
        while idx>=0:
            middle.next=middle_queue[idx]
            middle=middle.next
            idx-=1

        # concat
        middle.next=None
        middle_head=middle_head.next
        front.next=middle_head
        middle.next=back_head.next
        back.next=None
        return front_head.next
