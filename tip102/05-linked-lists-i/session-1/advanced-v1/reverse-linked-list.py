# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        stack = []
        current = head
        res = []
        while current:
            stack.append(current)
            current = current.next
        res = ListNode(stack.pop())
        while stack:
            prev = current
            current = current.next
            next = current.next

            prev, next = next, prev
        return res

prev = None
current = head
next = head.next

prev = current
current = current.next
next = current.next

prev, next = next, prev