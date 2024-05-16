# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while p2.next:
            if p2.next.next:
                p2 = p2.next.next
            else:
                p2 = p2.next
            p1 = p1.next
        return p1