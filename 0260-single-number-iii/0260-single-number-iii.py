class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ones =[]
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                ones.append(nums[i])
        return ones
        