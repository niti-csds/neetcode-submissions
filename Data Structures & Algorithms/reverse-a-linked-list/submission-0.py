# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = None
        curr = head
        while curr:
            loop = curr.next
            curr.next = ptr
            ptr = curr
            curr = loop

            
        head = ptr
        return ptr

obj = Solution()
head = ListNode(3, ListNode(2, ListNode(1, ListNode(0))))
print(obj.reverseList(head))
