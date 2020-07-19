"""
MEDIUM 162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
#O(Log n)
class Solution:
    def findPeakElement(self, nums: '''List[int]''') -> int:
        top = len(nums)-1
        if top == 0: return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        low = 0
        while low <= top:
            mid = (top + low) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid-1]:
                top = mid - 1
            else:
                low = mid + 1
#O(n) Solution    
        """
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]: return 0
            else: return 1
        if nums[0] > nums[1]: return 0
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        return len(nums)-1
        """