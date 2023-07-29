# 21. Merge Two Sorted List - Easy

import collections

# My answer - Fail to solve
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        node = list1
        node2 = list2
        
        while node is not None:
            tmp: ListNode = ListNode(node.val)
            node2 = list2

            while node2 is not None:
                if node2.next is not None: 
                    if tmp.val >= node2.val and tmp.val < node2.next.val:
                        node2.next, tmp.next = tmp, node2.next
                        break
                elif tmp.val >= node2.val:
                    node2.next = tmp
                    break
                elif tmp.val < node2.val:
                    tmp.next = node2
                    list2 = tmp
                    break
                node2 = node2.next
                
            node = node.next
        return list2

# Study Book - 1. Linkig w/ Recursion 
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    
l13 = ListNode(3)
l12 = ListNode(-9, l13)
# l11 = ListNode(1, l12)
l23 = ListNode(7)
l22 = ListNode(5, l23)
# l21 = ListNode(1, l22)

sol = Solution()
print(sol.mergeTwoLists(l12, l22))