#!/usr/bin/env python
class Solution(object):
    def __init__(self):
	self.result = []

    def findDiagonalOrder(self, matrix):
	rows = len(matrix)
	if rows == 0:
	    return matrix
	columns = len(matrix[0])
	def findnextup(x, y, columns):
	    if y == columns - 1:
		x = x + 1
		change = 1
	    elif x == 0:
		y = y + 1
		change = 1
	    else:
		x = x - 1
		y = y + 1
		change = 0
	    return x, y, change
	def findnextdown(x, y, rows):
	    if x == rows - 1:
		y = y + 1
		change = 1
	    elif y == 0:
		x = x + 1
		change = 1
	    else:
		x = x + 1
		y = y - 1
		change = 0
	    return x, y, change

	def findnext(x, y, rows, columns, mode):
	    print x, y
	    print matrix[x][y]
	    self.result.append(matrix[x][y])
	    if (x==rows-1)and(y==columns-1):
		return self.result
	    else:
	    	if mode:
		    x, y, change = findnextup(x, y, columns)
	    	else:
		    x, y, change = findnextdown(x, y, rows)
	    
		if change:
		    mode = not mode 

		return findnext(x, y, rows, columns, mode) 
	return findnext(0, 0, rows, columns, 1)		
s = Solution()
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
e = [1, 2, 3]
d = []
print s.findDiagonalOrder(d)		
