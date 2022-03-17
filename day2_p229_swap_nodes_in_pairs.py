# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(0)

        while head and head.next:
            next = head.next
            head.next = next.next
            next.next = head

            prev.next = next

            prev = head
            head = head.next

        return root.next