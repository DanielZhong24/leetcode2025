#2025-6-5 time: 5:15
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        if target in nums:
            return nums.index(target)
        
        
        for i in range(len(nums)):
            if nums[i] > target:
                return i 
            
        return len(nums)
        