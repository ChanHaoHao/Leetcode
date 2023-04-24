# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ans=ListNode(0, None)
        # tmp=ans
        # while list1!=None and list2!=None:
        #     if list1.val>list2.val:
        #         tmp.next=ListNode(list2.val, None)
        #         tmp=tmp.next
        #         list2=list2.next
        #     else:
        #         tmp.next=ListNode(list1.val, None)
        #         tmp=tmp.next
        #         list1=list1.next
        # if list1!=None:
        #     tmp.next=list1
        # elif list2!=None:
        #     tmp.next=list2
        # return ans.next
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val>list2.val:
            list2.next=self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next=self.mergeTwoLists(list1.next, list2)
            return list1