# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = None
        cur = head
        while(cur):
            r = cur.next
            cur.next = l
            l = cur
            cur = r
        return l
