#!/usr/bin/env python
class Solution(object):
    def twoSum(self, nums, target):
	result = []
	for x, first in enumerate(nums):
	    findnum = target - first
	    for second in nums[x+1:]:
		if findnum == second:
		    result.append([first, second])
	return result

    def threeSum(self, nums, target):
	result = []
	for z, three in enumerate(nums):
	    resulttmp = self.twoSum(nums[z+1:], target - three)
	    for ele in resulttmp:
	    	ele.append(three)
	    result += resulttmp
	return result
    	    	
    def fourSum(self, nums, target):
	result = []
	for k, four in enumerate(nums):
	    resulttmp = self.threeSum(nums[k+1:], target - four)
	    for ele in resulttmp:
	    	ele.append(four)
	    result += resulttmp
	return result

s = Solution()
a = [-3, -2, -1, 0, 0, 1, 2, 3]
print s.fourSum(a, 0)

	
		
	
