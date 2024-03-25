# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        
        # move fast two steps and slow one steps each time, so that slow will reach 
        # middle everytime fast reaches the end
        fast, slow = head.next.next, head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head