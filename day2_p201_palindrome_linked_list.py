# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 값을 저장할 배열 생성
        arr = []
        # 데크로 변경 가능
        # q : deque = collections.deque()
        curr = head

        # 배열에 값을 복사
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # 배열의 크기가 2보다 크면 앞 뒤로 꺼내서 비교하여 다르면 False 같으면 True 리턴
        while len(arr) > 1:
            # 데크 사용시
            # if arr.popleft != arr.pop()
            if arr.pop(0) != arr.pop():
                return False
        return True


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome_runner(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        rev = None

        while fast and fast.next:
            fast = fast.next.next
            rev = slow
            rev.next = rev
            slow = slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
