# 234. Palindrome Linked List - Easy

# My answer
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        node = head
        while node != None:
            lst.append(node.val)
            node = node.next            
        rev = lst[::-1]
        return lst == rev
    
l1 = ListNode(1)
l2= ListNode(2)
l3 = ListNode(2)
l4 = ListNode(1)
l1.next = l2
l2.next = l3
l3.next = l4

sol = Solution()
print(sol.isPalindrome(l1))