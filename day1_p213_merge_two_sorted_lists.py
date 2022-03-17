# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # head 리스트 노드 초기화
        head = ListNode(-1)
        # cursor는 시작 부분
        cursor = head

        # l1과 l2가 모두 존재한다면
        while l1 and l2:
            # l1의 값이 l2의 값보다 작다면
            if l1.val < l2.val:
                # cursor가 l1을 가리킴
                cursor.next = l1
                # l1이 가리키는 값으로 변경
                l1 = l1.next
            else:
                # cursor가 l2를 가리킴
                cursor.next = l2
                # l2가 가리키는 값으로 변경
                l2 = l2.next
            # 커서를 위에서 선정한 커서의 다음값으로 변경
            cursor = cursor.next

        # 마지막 노드 선정
        if l1:
            cursor.next = l1
        else:
            cursor.next = l2

        return head.next