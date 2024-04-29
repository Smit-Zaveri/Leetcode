class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

         
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] + 1 == target:
                return i + 1
            elif nums[i] - 1 == target and nums[i] - 1 != 0:
                return i
            elif target > nums[-1]:
                return len(nums)
            elif target < nums[0] :
                return 0
        
            
        