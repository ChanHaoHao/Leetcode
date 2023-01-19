# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(0)
        result=temp
        carry=0
        while l1 or l2 or carry!=0:
            sum=0
            
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
                
            sum+=carry
            temp.next=ListNode(sum%10)
            carry=int(sum/10)
            temp=temp.next
        print(temp,result)
        return result.next