#!/usr/bin/env python
class Solution(object):
    def isHappy(self, nums):
	left = 1
	right = len(nums) - 1
	while left < right:
	    while left < right:
		if nums[right] == nums[right-1]:
		    right -= 1
		else:
		    break
	    if nums[left] == nums[left-1]:
		tmp = nums[right]
		nums[right] = nums[left]
		nums[left] = tmp
	    else:
	    	left += 1

	print nums
	return left

a = [1, 1, 1]
s = Solution()
print s.isHappy(a)
