# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # use merge sort to merge k lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        # merge two sublists
        def merged_list(l1, l2):
            dummy = ListNode()
            node = dummy
            while l1 and l2:
                if l1.val>l2.val:
                    node.next = l2
                    l2 = l2.next
                else:
                    node.next = l1
                    l1 = l1.next
                node = node.next
            if l1:
                node.next = l1
            if l2:
                node.next = l2
            
            return dummy.next

        
        while len(lists)>1:
            mergedList = []
            for l in range(0, len(lists), 2):
                l1 = lists[l]
                if l+1<len(lists):
                    l2 = lists[l+1]
                else:
                    l2 = None
                
                mergedList.append(merged_list(l1, l2))
            lists = mergedList
        
        return lists[0]
