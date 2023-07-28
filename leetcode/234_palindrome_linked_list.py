# 234. Palindrome Linked List - Easy

import collections

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

# Study book - 1. conversion to list(queue) -> To know whether it is palindrome, I need a DS that front/back accesses are available
# q.pop(0) -> O(n) because list automatially shift all the elements of list to left (one slot) 
def isPalinedrome(head: ListNode) -> bool:
    q: list = []
    
    if not head:
        return True
    
    node = head

    while node is not None:
        q.append(node.val)
    
    while len(q) > 1:
        if q.pop() != q.pop(0):
            return False
    return True

# Study book - 2. Optimization w/ Deque
# Deque - Doubliy Linked List -> poping the first/last element takes O(1)
def isPalinedrome(head: ListNode) -> bool:
    q: collections.deque = collections.deque()
    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True

# Study book - 3. Runner Method**
#  
