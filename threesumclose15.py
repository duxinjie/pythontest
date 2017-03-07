#!/usr/bin/env python
class Solution(object):
    def isHappy(self, nums, target):
	if len(nums) < 3:
	    return False
	closest = nums[0] + nums[1] + nums[2]
	diff = abs(target - closest)
	nums.sort()
	for index in range(len(nums)-2):
	    left = index + 1
	    right = len(nums) - 1
	    while left < right:
		threesum = nums[index] + nums[left] + nums[right]
		newdiff = abs(threesum - target)
		if newdiff < diff:
		    diff = newdiff
		    closest = threesum
		if threesum < target:
		    left += 1
		else:
		    right -= 1
	return closest


s = Solution()
a = [0, 2, 1, -3]
print s.isHappy(a, 1)
	     		
