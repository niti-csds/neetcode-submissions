# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f_num ,s_num = 1, 1
        num_1 = 0
        num_2 = 0
        cur_1 = l1
        cur_2 = l2
        c_1,c_2 = 0,0
        total_digit = 0
        while(cur_1):
            num_1 += cur_1.val *f_num
            f_num *= 10
            cur_1 = cur_1.next
            c_1+=1
            
        while(cur_2):
            num_2 += cur_2.val * s_num
            s_num *= 10
            cur_2 = cur_2.next
            c_2 += 1
            
        total = num_1 + num_2
        dummy = ListNode(0)
        curr = dummy
        if total == 0:
            return dummy
        while(total>0):
            value = total%10
            curr.next = ListNode(value)
            curr = curr.next
            total = total//10 
        
        return dummy.next
        
            


        
