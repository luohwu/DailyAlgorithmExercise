# https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # link and new_link are used for traversal
        # head and new_head are reserved for reusing
        link=head
        new_head=new_link=Node(x=link.val)


        #table and new_table are used to track the index of each node in link and new_link
        table=[]
        new_table=[]
        table.append(link)
        new_table.append(new_link)
        #constructing the new link
        while link.next:
            link=link.next
            table.append(link)
            new_link.next=Node(val=link.val)
            new_link=new_link.next
            new_table.append(new_link)

        # record the index of node.random in link
        idx_random=[]
        link=head
        while link:
            idx_random.append(table.index(link.random))
            link=link.next
        new_link=new_head
        idx=0
        # copy the link.random to new_link.random
        while new_link:
            new_link.random=new_table[idx_random[idx]]
            idx+=1
            new_link=new_link.next

        return new_head




