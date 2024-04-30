class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        
        res = [int(x) for x in str(num + 1)]
        return res