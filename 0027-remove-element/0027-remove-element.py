class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            x=nums.remove(val)
        return len(nums)
        