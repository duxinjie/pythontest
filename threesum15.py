#!/usr/bin/env python
class Solution(object):
    def twoSum(self, nums, target):
	result = []
	for x, first in enumerate(nums):
	    findnum = target - first
	    for y in range(x+1, len(nums), 1):
		if findnum == nums[y]:
		    result.append([x, y])
#	    for y, second in enumerate(nums):
#		if findnum == second:
#		    if x < y:
#			result.append([x, y])
	return result

    def threeSum(self, nums, target):
	result = []
	for z, three in enumerate(nums):
	    resulttmp = self.twoSum(nums[z+1:], target - three)
	    for ele in resulttmp:
		ele[0] += z+1
		ele[1] += z+1
	    	ele.append(z)
#	    print resulttmp
	    result += resulttmp
	return result
	    	
s = Solution()
a = [1,3,-1, 0, -2, 5, 8, -4, -6, 3, 2, -2, 5, -7]
print s.threeSum(a, 0)

	
		
	
