#!/usr/bin/env python
class ListNode(object):
    def __init__(self, x):
	self.val = x
	self.next = None

class Solution(object):
    def printlist(self, head):
	while head:
	    print head.val
	    head = head.next

    def isHappy(self, head):
	if not head:
            return head
	start = head
	nextnode = head.next
	start.next = None
	while nextnode:
	    tmp = nextnode.next
	    nextnode.next = start
	    start = nextnode
	    nextnode = tmp
	return start	

a = ListNode(1)
print a
b = ListNode(2)
if a != b:
    print b
c = ListNode(4)
d = ListNode(5)
a.next = b
b.next = c
c.next = d
a = d
s = Solution()
s.printlist(a)
s.printlist(s.isHappy(a))
