
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def print_list(self,list):
        while list:
            if list.next:
                print(list.val, ' -> ', end='')
            else:
                print(list.val)
            list = list.next
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_head = head.next

        while even:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head


Solution().print_list(Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))



