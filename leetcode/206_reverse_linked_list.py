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

l5 = ListNode(5, None)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
sol = Solution()
print(sol.reverseList(l1))

