# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        count = 0
        length = 0
        curr = head
        replace = dummy
        while curr:
            length += 1
            curr = curr.next
        while count != (length - n):
            count += 1
            replace = replace.next
        replace.next = replace.next.next
        return dummy.next






        