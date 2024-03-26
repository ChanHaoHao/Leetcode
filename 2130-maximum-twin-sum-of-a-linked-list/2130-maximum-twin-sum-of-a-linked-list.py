# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum_list = [head.val]

        slow = head
        fast = head.next.next

        count = 0
        # using the fast, slow method to find the middle of the linkedlist
        while fast!=None and fast.next!=None:
            slow = slow.next
            sum_list.append(slow.val)
            fast = fast.next.next
            count += 1
        
        slow = slow.next

        # add the twin into the list
        while slow!=None:
            sum_list[count]+=slow.val
            slow = slow.next
            count-=1

        return max(sum_list)
