# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        # left 및 right 값 체크용
        count = 1

        while curr:
            # left <= count <= right 일 경우
            if count >= left and count <= right:
                # right값(rev 값의 head)에 도달시 head.next에 위치 저장
                if count == right:
                    head.next = curr
                # left값(rev 값의 tail)에 도달시 tail에 위치 저장
                if count == left:
                    tail = curr
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            # 범위 내에 없을 경우
            else:
                # prev에 현재 위치를 저장하고 다른 위치로 이동
                prev = curr
                curr = curr.next
            count += 1
        # while문에서 벗어나면 tail.next에 현재 위치(null)의 이전 위치를 저장
        tail.next = prev

        return head

    def reverseBetween_leetcode_solution(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, prev = head, None

        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        tail, con = cur, prev

        while right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            right -= 1

        con.next = prev
        tail.next = cur

        return head