# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        curr = head 
        while curr:
            curr = curr.next
            len += 1

        remove_index = len - n 
        if remove_index == 0:
            return head.next

        temp = head
        prev = None
        while remove_index > 0 :
            prev = temp
            temp = temp.next
            remove_index -= 1
        
        prev.next = temp.next


        return head
             
        