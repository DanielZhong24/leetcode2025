#2025-3-14 time: 11:18
class Solution(object):
    def threeSum(self, nums:list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1
            while left < right:
                s=nums[i]+nums[left]+nums[right]

                if s == 0 :
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return result
