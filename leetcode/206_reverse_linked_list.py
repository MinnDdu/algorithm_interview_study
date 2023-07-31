# 206. Reverse Linked List
import collections

# My answer
class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        stack = []
        while head:
            tmp = ListNode(head.val)
            stack.append(tmp)
            head = head.next

        rev_head = stack.pop()
        node = rev_head
        while stack:
            node.next = stack.pop()
            node = node.next

        return rev_head
    
    # Study book - 1. Fliping w/ recursive method
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
            # Base case
            if node is None:
                return prev
            next = node.next
            node.next = prev
            return reverse(next, node)
        return reverse(head)
            
    

    # Study book - 2. Fliping w/ iterative method
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
    

l5 = ListNode(5, None)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
sol = Solution()
print(sol.reverseList(l1))
