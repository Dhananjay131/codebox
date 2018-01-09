# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        root = ListNode(0)
        current = root
        while l1 and l2:
            if l1.val<=l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1: current.next = l1
        else: current.next = l2
        return root.next
                
