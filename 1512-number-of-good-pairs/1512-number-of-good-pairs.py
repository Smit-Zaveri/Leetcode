class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    n.append({i,j})
        return len(n)

        