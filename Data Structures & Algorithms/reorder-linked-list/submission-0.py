# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        l = head
        p = l
        # first mid find
        #left list = head-- mid
        #right list = last --- mid+1

        #fing length 
        while l:
            p = l
            l=l.next
            length += 1
        #p = last ele
        mid = length//2
        
        cur_mid = head
        while mid>0:
            cur_mid = cur_mid.next
            mid -= 1

        # reverse after mid_curr
        second = cur_mid.next
        cur_mid.next = None
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        while prev:
            temp1 = first.next
            first.next = prev
            temp2 = prev.next
            prev.next = temp1
            first = temp1
            prev = temp2
        
        return None

