# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        nodes = []
        while head:
            nodes.append(head)
            head = head.next
            if len(nodes)==k:
                for x in nodes[::-1]:
                    node.next = x
                    node = node.next
                nodes = []
        
        if len(nodes)>0:
            node.next = nodes[0]
        # to prevent loop in the linked node
        else:
            node.next = None
        return dummy.next