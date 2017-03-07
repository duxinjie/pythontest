#!/usr/bin/env python
class Solution(object):
    def __init__(self):
	self.result = 0
    def arrangeCoins(self,n):
	if n < 0:
	    return False
	a = 0
	while True:
	    if 2*n < a*(a + 1):
		break
	    a = a + 1
	return a-1
	
s = Solution()
print s.arrangeCoins(5)
