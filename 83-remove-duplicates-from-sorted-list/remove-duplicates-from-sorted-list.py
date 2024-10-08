# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values  = set()
        prev  = None
        curr = head
        while curr:
            if curr.val in values:
                prev.next  = curr.next
            else:
                values.add(curr.val)
                prev = curr
            curr = curr.next
        return head