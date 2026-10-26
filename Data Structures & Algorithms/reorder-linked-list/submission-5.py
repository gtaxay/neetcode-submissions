# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # every other
        # split in half
        # three parts (1. split half 2. revrse, combine?)


        #split half

        slow, fast = head, head
        # 1,2,3,4


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        # end first half
        slow.next = None

        #reverse
        # prev ends up as head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev will be shorter
        while prev:

            tempF = head.next
            tempS = prev.next

            head.next = prev
            prev.next = tempF
            prev = tempS
            head = tempF
        
    

        



        