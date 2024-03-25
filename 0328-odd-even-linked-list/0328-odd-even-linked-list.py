# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        oddElements = head
        evenElements = head.next
        even_start = head.next
        # if evenElements exist, means that odd.next.next should exist or at least the end of the linkedList
        # if evenElements.next exist, means that evenElements.next.next should exist or at least the end of the
        # linkedList
        while evenElements and evenElements.next:
            oddElements.next = oddElements.next.next
            oddElements = oddElements.next
            evenElements.next = evenElements.next.next
            evenElements = evenElements.next
        
        oddElements.next = even_start
        return head