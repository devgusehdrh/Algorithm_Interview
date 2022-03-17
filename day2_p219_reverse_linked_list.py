# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev 선언, curr는 head
        prev, curr = None, head

        # curr가 존재하는 동안
        while curr:
            # 다음 값 저장
            next = curr.next
            # 리스트 연결 방향 변경 curr -> prev
            curr.next = prev
            # prev를 curr로 변경
            prev = curr
            # curr를 next 값으로 변경
            curr = next
        # while문이 다 돌면 head는 prev가 된다
        return prev