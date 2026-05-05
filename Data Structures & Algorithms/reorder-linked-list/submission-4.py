# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        slow, fast = head, head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # cut off list 1 from 2
        curr = slow.next
        slow.next = None
        prev = None

        # revese second list
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp

        
        # merge lists

        while prev:
            ft = head.next
            bt = prev.next

            head.next = prev
            prev.next = ft
            head = ft
            prev = bt
        


        
            
        
        
