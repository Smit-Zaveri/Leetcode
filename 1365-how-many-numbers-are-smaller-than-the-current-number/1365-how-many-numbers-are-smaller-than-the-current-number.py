class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        current_number_less = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j]:
                    current_number_less = current_number_less + 1
            out.append(current_number_less)
            current_number_less = 0
        return out
        