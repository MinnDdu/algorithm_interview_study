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
    
    # Study book - 1. Data Structure Conversion
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> []:
        def toList(lst: ListNode) -> [int]:
            result: [] = []
            while lst:
                result.append(lst.val)
                lst = lst.next
            return result

        def reverseList(lst: ListNode) -> ListNode:
            node: ListNode = lst
            prev: ListNode = None

            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev

        def toReversedLinkedList(result: str) -> ListNode:
            prev: ListNode = None
            for c in result:
                node: ListNode = ListNode(c, prev)
                prev = node
            return prev
        
        a = toList(reverseList(l1))
        b = toList(reverseList(l2))

        result = int(''.join(str(c) for c in a)) + int(''.join(str(c) for c in b))
        return toReversedLinkedList(str(result))




    # Study book - 2. Circuit Theory - Full Adder (전가산기) - Quotient(몫)은 Carry Out(자리올림수)로, Remainder(나머지)는 결과로 택하는 전체적인 Full Adder의 컨셉 이용
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # carry, val = (sum + carry) // 10, (sum + carry) % 10
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next


l3 = ListNode(3, None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

ll2 = ListNode(2, None)
ll1 = ListNode(1, ll2)
sol = Solution()
print(sol.addTwoNumbers(l1, ll1))