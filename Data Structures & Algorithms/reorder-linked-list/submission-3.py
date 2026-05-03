# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse back half

        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        first, second = head, prev

        while second:
            tempF = first.next
            tempS = second.next

            first.next = second
            second.next = tempF

            first = tempF
            second = tempS




        


        