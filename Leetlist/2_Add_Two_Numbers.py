# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        head1 = l1
        head2 = l2
        head = head1

        def helper(node, rem):
            head = node
            while node:
                summ = node.val + rem
                node.val = summ % 10
                rem = summ // 10
                tail = node
                node = node.next
            return head, tail, rem

        while l1 and l2:
            summ = l1.val + l2.val + rem
            l1.val = summ % 10
            l2.val = summ % 10
            rem = summ // 10
            tail = l1
            l1 = l1.next
            l2 = l2.next

        if l1:
            head = head1
            l1, tail, rem = helper(l1, rem)

        elif l2:
            head = head2
            l2, tail, rem = helper(l2, rem)
        if rem > 0:
            tail.next = ListNode(rem)
        return head