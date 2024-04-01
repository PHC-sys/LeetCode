# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        head, head.next = ListNode(0), head
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else: p = p.next
        return head.next