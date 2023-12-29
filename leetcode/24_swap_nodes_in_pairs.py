# 24. Swap Nodes in Pairs - Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # My answer - iterative swap
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ListNode(None)
        root = prev
        prev.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            prev.next = tmp

            prev = head
            head = head.next
        return root.next
    
    # Study book - 1. recursive swap
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            ptr = head.next
            head.next = self.swapPairs(ptr.next) # like head.next = haed.next.next
            ptr.next = head # like prev.next = head
            return ptr
        return head
