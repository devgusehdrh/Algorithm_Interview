# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 값을 저장할 배열 생성
        arr = []
        curr = head

        # 배열에 값을 복사
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # 배열의 크기가 2보다 크면 앞 뒤로 꺼내서 비교하여 다르면 False 같으면 True 리턴
        while len(arr) > 1:
            if arr.pop(0) != arr.pop():
                return False
        return True