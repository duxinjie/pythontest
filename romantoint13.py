#!/usr/bin/env python
class Solution(object):
    def __init__(self):
	self.romanku = {}
	self.romanku['I'] = 1
	self.romanku['V'] = 5
	self.romanku['X'] = 10
	self.romanku['L'] = 50
	self.romanku['C'] = 100
	self.romanku['D'] = 500
	self.romanku['M'] = 1000
	self.romankuindex = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
	print self.romanku
    def romanToInt(self, s):
	index = 0
	result = 0
	while True:
	    if self.romankuindex.index(s[index]) < self.romankuindex.index(s[index+1]):
		result += self.romanku[s[index+1]] - self.romanku[s[index]]
		index += 2
	    elif self.romankuindex.index(s[index]) == self.romankuindex.index(s[index+1]):
	        if self.romankuindex.index(s[index]) == self.romankuindex.index(s[index+2]):
		    result += self.romanku[s[index]] * 3
		    index += 3
	    	else:
		    result += self.romanku[s[index]] * 2
		    index += 2
	    else:
		result += self.romanku[s[index]]
		index += 1	
	    if index == len(s):
		break

	return result

s = Solution()
a = 'MMMCMXLIX'
print s.romanToInt(a)

	
