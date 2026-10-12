# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        l2 = slow.next
        prev = slow.next = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
        l2 = prev

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
