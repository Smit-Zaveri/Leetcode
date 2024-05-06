class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans1, ans2 = nums[:n], nums[n:]
        re = []
        for i in range(n):
            re.extend([ans1[i], ans2[i]])
        return re