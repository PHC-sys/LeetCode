# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        re = [head.val]
        while head.next:
            head = head.next
            re.append(head.val)
        for i,v in enumerate(re):
            if v != re[len(re)-i-1]:
                return False
        return True