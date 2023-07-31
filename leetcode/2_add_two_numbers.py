# 2. Add Two Numbers = Medium
import collections

# My answer
class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digits1 = 0
        digits2 = 0
        len1 = 0
        len2 = 0
        tmp1 = l1
        tmp2 = l2

        while tmp1:
            len1 += 1
            tmp1 = tmp1.next
        while tmp2:
            len2 += 1
            tmp2 = tmp2.next
            
        for i in range(len1):
            digits1 += l1.val * (10**i) # flip
            l1 = l1.next
        for i in range(len2):
            digits2 += l2.val * (10**i) # flip
            l2 = l2.next
            
        digits1 += digits2
        str_digits1 = str(digits1)

        if digits1 == 0:
            return ListNode(0)

        node = None
        for i in range(len(str_digits1)):
            val = int(str_digits1[i])
            prev = node            
            node = ListNode(val, prev)

        return node

l3 = ListNode(3, None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

ll2 = ListNode(2, None)
ll1 = ListNode(1, ll2)
sol = Solution()
print(sol.addTwoNumbers(l1, ll1))