# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        heads = []
        while head:
            heads.append(head)
            if head.next in heads:
                return True
            head = head.next

        return False


        